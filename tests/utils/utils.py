from playwright.sync_api import Page

def is_mobile(page:Page):
    desktop = 992
    is_mobile = False

    if(page.viewport_size['width']<desktop):
        is_mobile = True
    
    return is_mobile