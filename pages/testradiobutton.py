import pytest
from playwright.sync_api import sync_playwright

from pages.radiobuttonpage import radiobuttonpage


def test_radiobuttonp():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        login_page = radiobuttonpage(page)
        login_page.gotourl("https://demoqa.com/radio-button")
        login_page.radiobuttonpageone()
        browser.close()
