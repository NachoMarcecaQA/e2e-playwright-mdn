from playwright.sync_api import Page, expect
from utils.constants import HOME_PAGE

#Homepage 
def go_to_homepage(page: Page):
    print("Given the user visits homepage")
    page.goto(HOME_PAGE)

#Navigation Bar (NavBar)
def click_references_link(page: Page):
    print("And clicks on References")
    page.get_by_role("link", name="References", exact=True).click()

    print("Then the user should be on References page")
    expect(page).to_have_url("https://developer.mozilla.org/en-US/docs/Web")
    expect(page).to_have_title("Web technology for developers | MDN")
    expect(page.get_by_role("heading", name="Overview / Web Technology", exact=True)).to_be_visible

def click_learn_link(page: Page):
    print("And clicks on Learn")
    page.get_by_role("link", name="Learn", exact=True).click()

    print("Then the user should be on Learn page")
    expect(page).to_have_url("https://developer.mozilla.org/en-US/docs/Learn_web_development")
    expect(page).to_have_title("Learn web development | MDN")
    expect(page.get_by_role("heading", name="Overview / Web Technology", exact=True)).to_be_visible

def click_plus_link(page: Page):
    print("And clicks on Plus")
    page.get_by_role("link", name="Plus", exact=True).click()

    print("Then the user should be on Plus page")
    expect(page).to_have_url("https://developer.mozilla.org/en-US/plus")
    expect(page).to_have_title("MDN Plus")
    expect(page.get_by_role("heading", name="Overview / Web Technology", exact=True)).to_be_visible

def click_curriculum_link(page: Page):
    print("And clicks on Curriculum")
    page.get_by_role("link", name="Curriculum New", exact=True).click()

    print("Then the user should be on Curriculum page")
    expect(page).to_have_url("https://developer.mozilla.org/en-US/curriculum/")
    expect(page).to_have_title("MDN Curriculum")
    expect(page.get_by_role("heading", name="Overview / Web Technology", exact=True)).to_be_visible

def click_blog_link(page: Page):
    print("And clicks on Blog")
    page.get_by_label("Main menu", exact=True).get_by_role("link", name="Blog").click()

    print("Then the user should be on Blog page")
    expect(page).to_have_url("https://developer.mozilla.org/en-US/blog/")
    expect(page).to_have_title("MDN Blog")
    expect(page.get_by_role("heading", name="Overview / Web Technology", exact=True)).to_be_visible

def click_tools_link(page: Page):
    print("And clicks on Tools")
    page.get_by_role("button", name="Tools").click()
    page.get_by_role("link", name="Playground Write, test and").click()

    print("Then the user should be on Tools page")
    expect(page).to_have_url("https://developer.mozilla.org/en-US/play")
    expect(page).to_have_title("Playground | MDN")
    expect(page.get_by_role("heading", name="Overview / Web Technology", exact=True)).to_be_visible
