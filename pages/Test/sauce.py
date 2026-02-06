from playwright.sync_api import Page, Expect, expect
class saucelogin:
    def __init__(self,page:Page):
        self.page=page
        self.usernamesau1=page.locator("[id=\"user-name\"]")
        self.passwordsau2=page.locator("[id=\"password\"]")
        self.login1=page.locator("[id=\"login-button\"]")
          
    def sauselogin(self,username,password):
        #self.page.once("dialog",lambda d: d.accept("testing"))
        #self.page.pause()
       # self.usernamesau1.wait_for(state="visible")
        try:
            self.usernamesau1.fill(username)
            self.passwordsau2.fill(password)
            self.login1.click()
        except TimeoutError:
            print("page not loading")

        self.page.wait_for_url("https://www.google.com/")
        self.page.wait_for_timeout(5000) # to wait to explicitly


    def get_cookies(self):
        cookies=self.page.context.cookies()
        return cookies
    
    def add_cookies(self,name:str,value:str,url:str):
        self.page.context.add_cookies([{
            "name": name,
            "value": value,
            "domain": url,
            "path": "/",
        }])
    def getlocalstorage(self):
        return self.page.evaluate("()=>window.localStorage")
    
    def setlocalstorage(self,key,value):
        self.page.evaluate(f"()=> window.localStorage.setItem('{key}', '{value}')")

    def clearlocalstorage(self):
        self.page.evaluate("()=>window.localStorage.clear()")
