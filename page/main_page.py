from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Main_page:

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(app.wd, 2)

    def mp_open(self):
        wd = self.app.wd
        wd.get('http://localhost/litecart/public_html/en/')

    def mp_open_first_product(self):
        wd = self.app.wd
        wait = self.wait
        elements = wd.find_elements_by_css_selector('li.product.column.shadow.hover-light img')
        elements[0].click()
        # ожидание появления блока с информацией #
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tab-information")))
