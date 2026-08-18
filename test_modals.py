import pytest
from playwright.sync_api import sync_playwright
from pages.Test.Modals import Modals

from pages.Test.facebookloginpage import facebookloginpage
def test_modals():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        loginpage=facebookloginpage(page)
        loginpage.gotourl("https://demoqa.com/modal-dialogs")
        Modals1=Modals(page)
        Modals1.handle_Modals()
        page.pause()