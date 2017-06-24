from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Cart_page:

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(app.wd, 2)

    def cart_checkout(self):
        wd = self.app.wd
        wait = self.wait
        wd.find_element_by_css_selector('a[href$="checkout"][class=link]').click()
        # ожидание появления кнопки 'удалить' #
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="remove_cart_item"]')))
        # ожидание пока обновится заголовок #
        wait.until(EC.title_is('Checkout | My Store'))

    def elements_in_table(self):
        wd = self.app.wd
        elements = wd.find_elements_by_css_selector(
            '#order_confirmation-wrapper tr:not([class="header"]):not([class="footer"]) td[style="text-align: center;"]')
        l = []
        for row in elements:
            k = row
            l.append(k)
        return l

    def remove_product(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('button[name="remove_cart_item"]').click()

    def remove(self, elements_in_table):
        wd = self.app.wd
        wait = self.wait
        for i in range(len(elements_in_table)):
            first_value_in_table = wd.find_element_by_css_selector(
                'tr:not([class="header"]):not([class="footer"]) td[style="text-align: center;"]')
            self.app.cp.remove_product()
            try:
                # ожидание изменения первого элемента таблицы #
                wait.until(EC.staleness_of(first_value_in_table))
                print('Количество уток поубавилось')
            except Exception as txt:
                print('Исключение =', txt)

    def is_finish(self):
        wd = self.app.wd
        wait = self.wait
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-cart-wrapper a[href$="/public_html/en/"]')))
