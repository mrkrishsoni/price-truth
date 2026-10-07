"""Methods, data sources, model quality and limits."""
from price_truth.resources import report
from price_truth.ui import methods_page

methods_page(report("model_evaluation.json"), report("current/model_audit.json"), report("data_audit.json"))
