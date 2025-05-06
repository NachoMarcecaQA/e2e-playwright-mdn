from playwright.sync_api import Page, expect    
from helpers.navigation import go_to_homepage


def test_search_happy_path (page: Page):
    go_to_homepage(page)
    print("And clicks on Search bar")
    page.locator("#hp-search-input").click()
    print("And fills with Learn")
    page.locator("#hp-search-input").fill("Learn")
    print("And hits Enter button")
    #page.locator("#hp-search-input").press("Enter")
    page.locator("#hp-search-form").get_by_role("button", name="Search").click()

    print("Then the user should see Search results for Learn")
    expect(page).to_have_url("https://developer.mozilla.org/en-US/search?q=Learn")
    expect(page.get_by_role("heading", name="Search results for: Learn")).to_be_visible


def test_search_text_too_long (page: Page):
    go_to_homepage(page)
    print("And clicks on Search bar")
    page.locator("#hp-search-input").click()
    print("And searches with a long value")
    page.locator("#hp-search-input").fill("softwareTestingEnsuresThatApplicationsFunctionAsIntendedByIdentifyingBugsAndVerifyingRequirementsItIncludesUnitTestsIntegrationTestsAndEndToEndTestsAutomatedTestingImprovesEfficiencyWhileManualTestingCatchesEdgeCasesAndValidatesUserExperienceAcrossDevices")
    print("And hits Enter button")
    #page.locator("#hp-search-input").press("Enter")
    page.locator("#hp-search-form").get_by_role("button", name="Search").click()

    print("Then the user should see an error message")
    expect(page.locator("b")).to_contain_text("Ensure this value is less than or equal to 200.")