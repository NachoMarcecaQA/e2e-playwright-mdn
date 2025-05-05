from playwright.sync_api import Page
from helpers.navigation import go_to_homepage, click_references_link, click_blog_link, click_curriculum_link, click_learn_link, click_plus_link, click_tools_link

def test_homepage_navbar(page: Page):
    go_to_homepage(page)
    click_references_link(page)
    click_learn_link(page)
    click_plus_link(page)
    click_curriculum_link(page)
    click_blog_link(page)
    click_tools_link(page)
