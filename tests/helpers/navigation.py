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
    print(
        "And clicks on References"
        )
    page.get_by_role(
        "link", 
        name="References", 
        exact=True
        ).click()

def click_learn_link(page: Page):
    print(
        "And clicks on Learn"
        )
    page.get_by_role(
        "link", 
        name="Learn", 
        exact=True
        ).click()
    
def click_plus_link(page: Page):
    print(
        "And clicks on Plus"
        )
    page.get_by_role(
        "link", 
        name="Plus", 
        exact=True
        ).click()
    
#fix all selectors below
def click_curriculum_link(page: Page):
    print(
        "And clicks on Curriculum"
        )
    page.get_by_role(
        "link", 
        name="Curriculum", 
        exact=True
        ).click()
    
def click_blog_link(page: Page):
    print(
        "And clicks on Blog"
        )
    page.get_by_role(
        "link", 
        name="Blog", 
        exact=True
        ).click()
    
def click_tools_link(page: Page):
    print(
        "And clicks on Tools"
        )
    page.get_by_role(
        "link", 
        name="Tools", 
        exact=True
        ).click()
    
# idea for clicking every item in each section
#     for li in page.get_by_role('listitem').all():
#   li.click();