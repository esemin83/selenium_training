#from selenium.webdriver.chrome.webdriver import WebDriver
#from selenium.webdriver.ie.webdriver import WebDriver
#from selenium.webdriver.safari.webdriver import WebDriver
from selenium import webdriver

from fixture.admin_console import Admin_console
from fixture.session import Session
from fixture.litecart import Litecart


class Application:

    def __init__(self):
        #browser_path = "C:\\Program Files (x86)\\Nightly\\firefox.exe"
        #browser_path = "C:\\Program Files\\Firefox_53\\firefox.exe"
        #self.wd = webdriver.Firefox(firefox_binary=browser_path)
        #self.wd.maximize_window()
        #self.wd.implicitly_wait(3)
        #print(self.wd.capabilities)

        self.wd = webdriver.Chrome()
        #self.wd = webdriver.Ie()
        #print(self.wd.capabilities)

        # неявное ожидание #
        #self.wd.implicitly_wait(3)

        self.adm = Admin_console(self)
        self.session = Session(self)
        self.lt = Litecart(self)

    def destroy(self):
        self.wd.quit()
