import pytest
import json
from playwright.sync_api import sync_playwright
from pages.Test.sauce import saucelogin

from pages.Test.facebookloginpage import facebookloginpage
def test_sauce():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        # with open("cookies.json","r")as f:
        #     cookies=json.load(f)
        #     context.add_cookies(cookies)
        # context.clear_cookies()

        page = context.new_page()
        sauce1=saucelogin(page)
        #sauce1.add_cookies("session-username","standard_user","www.saucedemo.com/")
        loginpage=facebookloginpage(page)
        try:
            loginpage.gotourl("https://www.saucedemo.com/.inventory.html")
        except TimeoutError:
            print("page doesnt load")
            page.screenshot(path="screenshot/login.png")

        #loginpage.gotourl("https://www.saucedemo.com/")
        
        sauce1.sauselogin("standard_user","secret_sauce")
    
        page.pause()

        #cookies=sauce1.get_cookies()
        #print(cookies)