import pytest
from playwright.sync_api import sync_playwright
from pages.Test.demobuttons import demobuttons
def test_demobuttons():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        loginpage=demobuttons(page)
        loginpage.gotourl("https://demoqa.com/buttons/")
        loginpage.clickme_click()
        page.pause()