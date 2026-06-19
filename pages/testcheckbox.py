import pytest
from playwright.sync_api import sync_playwright

from pages.checkbox import checkbox


def test_checkboxpage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        login_page = checkbox(page)
        login_page.gotourl("https://demoqa.com/checkbox")
        login_page.checkboxpage()

        browser.close()