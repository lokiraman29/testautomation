import pytest
from playwright.sync_api import sync_playwright
from pages.Test.frames import frames
from pages.Test.facebookloginpage import facebookloginpage
def test_frames():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        loginpage=facebookloginpage(page)
        loginpage.gotourl("https://demoqa.com/frames/")
        frame=frames(page)
        frame.clickme_click()
        page.pause()