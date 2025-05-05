from playwright.sync_api import Page
from helpers.navigation import go_to_homepage

def test_visit_homepage (page: Page):
    go_to_homepage(page)

