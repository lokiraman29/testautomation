import pytest
from playwright.sync_api import sync_playwright

from pages.demotextboxpage import demotextboxpage


def test_testdemotextboxpageone():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        login_page = demotextboxpage(page)
        login_page.gotourl("https://demoqa.com/text-box")
        login_page.demotextboxpageone("John","john.doe@example.com","123 Main Street","456 Elm Street")
        browser.close()
