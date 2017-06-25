#from selenium.webdriver.chrome.webdriver import WebDriver
#from selenium.webdriver.ie.webdriver import WebDriver
#from selenium.webdriver.safari.webdriver import WebDriver
from selenium import webdriver
from fixture.admin_console import Admin_console
from fixture.session import Session
from fixture.litecart import Litecart
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from page.main_page import Main_page
from page.product_page import Product_page
from page.cart_page import Cart_page


class Application:

    def __init__(self):
        #browser_path = "C:\\Program Files (x86)\\Nightly\\firefox.exe"
        #browser_path = "C:\\Program Files\\Firefox_53\\firefox.exe"
        #self.wd = webdriver.Firefox(firefox_binary=browser_path)
        #self.wd.maximize_window()
        #self.wd.implicitly_wait(3)
        #print(self.wd.capabilities)

        self.wd = webdriver.Chrome()#(desired_capabilities={'browser': 'ALL'})
        #self.wd = webdriver.Ie()
        #print(self.wd.capabilities)

        # протооколирование #
        #self.wd = EventFiringWebDriver(webdriver.Chrome(desired_capabilities={'unexpectedAlertBehaviour': 'dismiss'}), MyListener())
        print(self.wd.capabilities)

        # лог браузера + протооколирование - только для хрома??? #
        #d = DesiredCapabilities.CHROME
        #d['loggingPrefs'] = {'browser': 'ALL'}

        # proxy #
        #d['proxy'] = {"proxyType": "MANUAL", "httpProxy": "localhost:8888"}

        #self.wd = EventFiringWebDriver(webdriver.Chrome(desired_capabilities=d), MyListener())
        #self.wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())

        # remote #
        #self.wd = webdriver.Remote("http://192.168.1.107:4444/wd/hub", desired_capabilities={"browserName": "internet explorer"})
        #self.wd = webdriver.Remote("http://192.168.1.107:4444/wd/hub",
        #                           desired_capabilities={"browserName": "chrome"})

        # неявное ожидание #
        #self.wd.implicitly_wait(3)

        self.adm = Admin_console(self)
        self.session = Session(self)
        self.lt = Litecart(self)
        self.mp = Main_page(self)
        self.pp = Product_page(self)
        self.cp = Cart_page(self)

    def destroy(self):
        self.wd.quit()

    # класс протоколирования #


class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)
