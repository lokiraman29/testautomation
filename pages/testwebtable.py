import pytest
from playwright.sync_api import sync_playwright

from pages.webtablepage import webtablepage


def test_testwebtable():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        login_page = webtablepage(page)
        login_page.gotourl("https://demoqa.com/webtables")
        login_page.webtablepageone("John", "Doe", "john.doe@example.com", "30", "50000", "IT")
        browser.close()