from playwright.sync_api import Page
from utils.constants import HOME_PAGE

def go_to_homepage(page: Page):
    print(
        "Given the user visits homepage"
        )
    page.goto(
        HOME_PAGE
        )

def click_references_link(page: Page):
    page.get_by_role(
        "link", 
        name="References", 
        exact=True
        ).click()
