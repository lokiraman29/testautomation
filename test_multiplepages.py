import pytest
from playwright.sync_api import sync_playwright
from pages.Test.facebookloginpage import facebookloginpage
from pages.Test.newtab import pwa_newtab
def test_facebook():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        loginpage=facebookloginpage(page)
        newtab=pwa_newtab(page)
        loginpage.gotourl("https://demoqa.com/browser-windows")

        page1=newtab.click_newtab()
        loginpage1=facebookloginpage(page1)
        loginpage1.gotourl("https://www.facebook.com/")
        loginpage1.createnewaccount_click()
        loginpage1.createnewaccount_action("test","facebook","2","5","1993","9546211223")