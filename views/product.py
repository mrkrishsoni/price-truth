"""Price check page."""
from price_truth.resources import catalogue, model
from price_truth.ui import product_page

product_page(catalogue(), model)
