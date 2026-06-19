import pytest
from playwright.sync_api import sync_playwright

from pages.linkpage import linkpage


def test_testlink():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        login_page = linkpage(page)
        login_page.gotourl("https://demoqa.com/links")
        login_page.linkspageone()
        browser.close()