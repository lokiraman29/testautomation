
import pytest
from playwright.sync_api import sync_playwright

from pages.demobuttonspage import demobuttonspage


def test_testdemobuttons():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        login_page = demobuttonspage(page)
        login_page.gotourl("https://demoqa.com/buttons")
        login_page.demobuttonsmethod()
        browser.close()