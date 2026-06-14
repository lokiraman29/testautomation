import pytest
from playwright.sync_api import sync_playwright

from pages.demoqaform import demoqaform


def test_demoqaformpage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        login_page = demoqaform(page)
        login_page.gotourl("https://demoqa.com/automation-practice-form/")
        login_page.demoqaformpage("John","Doe","john.doe@example.com","1234567890",'Maths','Sports',"123 Main Street",)
        browser.close()
