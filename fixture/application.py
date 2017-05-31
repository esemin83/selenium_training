#from selenium.webdriver.chrome.webdriver import WebDriver
#from selenium.webdriver.ie.webdriver import WebDriver
#from selenium.webdriver.safari.webdriver import WebDriver
from selenium import webdriver

from fixture.admin_console import Admin_console
from fixture.session import Session


class Application:

    def __init__(self):
        #self.wd = WebDriver()

        #self.wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
        #self.wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
        #print(self.wd.capabilities)

        ### ChromeOptions ###

        #options = webdriver.ChromeOptions()
        #options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        #options.add_argument("start-maximized")

        #self.wd = webdriver.Chrome(chrome_options=options)
        #print(self.wd.capabilities)

        ### Firefox Nightly###

        #self.wd = webdriver.Firefox(firefox_binary="C:\\Program Files (x86)\\Nightly\\firefox.exe")
        #print(self.wd.capabilities)

        browser_path = "C:\\Program Files (x86)\\Nightly\\firefox.exe"
        #browser_path = "C:\\Program Files\\Firefox_53\\firefox.exe"
        self.wd = webdriver.Firefox(firefox_binary=browser_path)
        #self.wd.maximize_window()
        self.wd.implicitly_wait(3)
        print(self.wd.capabilities)

        self.adm = Admin_console(self)
        self.session = Session(self)

    def destroy(self):
        self.wd.quit()
