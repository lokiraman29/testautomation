import pytest
from playwright.sync_api import sync_playwright
from pages.Test.alerts import alert

from pages.Test.facebookloginpage import facebookloginpage
@pytest.mark.smoke # use this tag when to run specific file  
def test_alerts():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        loginpage=facebookloginpage(page)
        loginpage.gotourl("https://demoqa.com/alerts/")
        alerts1=alert(page)
        alerts1.handle_alerts()
        page.screenshot(path="screenshots/alerts.png")
        page.pause()