"""Portable Chrome workflow checks with explicit viewport coverage and retained evidence."""
import argparse
import json
import os
import time
from datetime import UTC, datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

from price_truth.paths import REPORTS

OUT = REPORTS / "current"


def check_workspace(page, out: Path = OUT) -> None:
    """Exercise the connected real-model flow through visible controls."""
    page.get_by_test_id("stSidebar").get_by_text("Product Workspace", exact=True).click()
    page.get_by_role("heading", name="Product Workspace", exact=True).wait_for()
    page.get_by_role("button", name="Assess price", exact=True).click()
    page.get_by_text("Advertised discount", exact=True).wait_for()
    download_button = page.get_by_role("button", name="Download assessment PDF", exact=True)
    download_button.wait_for()
    page.screenshot(path=str(out / "workspace-desktop.png"), full_page=True)
    with page.expect_download() as pending:
        download_button.click()
    pending.value.save_as(str(out / "browser-assessment.pdf"))
    assert (out / "browser-assessment.pdf").read_bytes().startswith(b"%PDF-")


def check_viewports(page, out: Path = OUT) -> list:
    """Measure overflow at three viewports; do not call emulation a physical-device test."""
    results = []
    for width, height in [(1440, 1000), (768, 1024), (390, 844)]:
        page.set_viewport_size({"width": width, "height": height})
        page.wait_for_timeout(400)
        page.screenshot(path=str(out / f"workspace-{width}.png"), full_page=True)
        overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
        results.append({"width": width, "height": height, "horizontal_page_overflow": overflow})
    return results


def main() -> None:
    """Exercise the local browser and save completed check evidence."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--browser", choices=["chrome", "firefox", "webkit"], default="chrome")
    args = parser.parse_args()
    out = OUT if args.browser == "chrome" else OUT / args.browser
    out.mkdir(parents=True, exist_ok=True)
    mac_chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    executable = os.environ.get("PRICE_TRUTH_CHROME") or (mac_chrome if Path(mac_chrome).exists() else None)
    with sync_playwright() as playwright:
        engine = playwright.chromium if args.browser == "chrome" else getattr(playwright, args.browser)
        browser = engine.launch(executable_path=executable if args.browser == "chrome" else None, headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1000})
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        start = time.perf_counter()
        page.goto(os.environ.get("PRICE_TRUTH_URL", "http://127.0.0.1:8501"))
        page.get_by_role("heading", name="Know what your price means").wait_for()
        load_seconds = time.perf_counter()-start
        check_workspace(page, out)
        viewports = check_viewports(page, out)
        result = {"generated_at": datetime.now(UTC).isoformat(), "browser": browser.version,
                  "initial_visible_load_seconds": load_seconds, "javascript_errors": errors,
                  "viewports": viewports, "flows": ["overview", "workspace real assessment", "actual PDF download"],
                  "scope": f"Local {args.browser}, three viewport emulations. WebKit is not branded Safari. No physical devices tested."}
        (out / "browser_check.json").write_text(json.dumps(result, indent=2))
        browser.close()
        assert not errors and not any(v["horizontal_page_overflow"] for v in viewports), result
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
