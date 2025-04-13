from playwright.sync_api import Page, expect
from helpers.navigation import go_to_homepage, click_references_link

def test_homepage_navbar(page: Page):
    go_to_homepage(page)
    click_references_link(page)
    

    

    

