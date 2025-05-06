from playwright.sync_api import Page, expect
from utils.constants import HOME_PAGE, SIGNUP_PAGE
from utils.utils import is_mobile
import time

#Signup
def go_to_signup(page: Page):
    print("Given the user visits signup page")
    page.goto(SIGNUP_PAGE)

#Homepage 
def go_to_homepage(page: Page):
    print("Given the user visits homepage")
    page.goto(HOME_PAGE)

#Navigation Bar (NavBar)
def click_references_link(page: Page):
    print("And clicks on References")
    if is_mobile(page):
        page.get_by_role("button", name="Open main menu").click()
        page.get_by_role("button", name="References").click()
        page.get_by_label("References").get_by_role("link", name="HTML").click()
        print("Then the user should be on References page")
        expect(page).to_have_url("https://developer.mozilla.org/en-US/docs/Web/HTML")
        expect(page).to_have_title("HTML: HyperText Markup Language | MDN")
    else:
        page.get_by_role("link", name="References").click()
        print("Then the user should be on References page")
        expect(page).to_have_url("https://developer.mozilla.org/en-US/docs/Web")
        expect(page).to_have_title("Web technology for developers | MDN")


def click_learn_link(page: Page):
    print("And clicks on Learn")
    if is_mobile(page):
        page.get_by_role("button", name="Open main menu").click()
        page.get_by_role("button", name="Learn").click()
        page.get_by_label("Learn").get_by_role("link", name="Overview / MDN Learning Area").click()
    else:
        page.get_by_role("link", name="Learn", exact=True).click()

    print("Then the user should be on Learn page")
    expect(page).to_have_url("https://developer.mozilla.org/en-US/docs/Learn_web_development")
    expect(page).to_have_title("Learn web development | MDN")

def click_plus_link(page: Page):
    print("And clicks on Plus")
    if is_mobile(page):
        page.get_by_role("button", name="Open main menu").click()
        page.get_by_role("button", name="Plus").click()
        page.get_by_label("Plus").get_by_role("link", name="Overview").click()
    else:    
        page.get_by_role("link", name="Plus", exact=True).click()

    print("Then the user should be on Plus page")
    expect(page).to_have_url("https://developer.mozilla.org/en-US/plus")
    expect(page).to_have_title("MDN Plus")


def click_curriculum_link(page: Page):
    print("And clicks on Curriculum")
    if is_mobile(page):
        page.get_by_role("button", name="Open main menu").click()

    page.get_by_role("link", name="Curriculum New", exact=True).click()

    print("Then the user should be on Curriculum page")
    expect(page).to_have_url("https://developer.mozilla.org/en-US/curriculum/")
    expect(page).to_have_title("MDN Curriculum")

def click_blog_link(page: Page):
    print("And clicks on Blog")
    if is_mobile(page):
        page.get_by_role("button", name="Open main menu").click()
    page.get_by_label("Main menu", exact=True).get_by_role("link", name="Blog").click()

    print("Then the user should be on Blog page")
    expect(page).to_have_url("https://developer.mozilla.org/en-US/blog/")
    expect(page).to_have_title("MDN Blog")

def click_tools_link(page: Page):
    print("And clicks on Tools")
    if is_mobile(page):
        page.get_by_role("button", name="Open main menu").click()
        page.get_by_role("button", name="Tools").click()
        page.get_by_label("Tools").get_by_role("link", name="Playground").click()
    else: 
        page.get_by_role("button", name="Tools").click()
        page.get_by_role("link", name="Playground Write, test and").click()

    print("Then the user should be on Tools page")
    expect(page).to_have_url("https://developer.mozilla.org/en-US/play")
    expect(page).to_have_title("Playground | MDN")
