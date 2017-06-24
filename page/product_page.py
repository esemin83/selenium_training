from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Product_page:

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(app.wd, 2)

    @property
    def select_is_present(self):
        wd = self.app.wd
        l = []
        try:
            e = wd.find_element_by_css_selector('select[name="options[Size]"]')
            l.append(e)
        except Exception:
            pass
        return len(l)

    def click_select(self):
        wd = self.app.wd
        select = Select(wd.find_element_by_css_selector('select[name="options[Size]"]'))
        select.select_by_value('Small')
        print('\n', 'Попалась выпадашка')

    @property
    def get_item_1(self):
        wd = self.app.wd
        x = int(wd.find_element_by_css_selector('span.quantity').get_attribute('innerText'))
        return x

    def click_add(self, new_value_of_item):
        wd = self.app.wd
        wait = self.wait
        wd.find_element_by_css_selector('button[name="add_cart_product"]').click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.quantity'), '%s' % new_value_of_item))

    @property
    def get_item_2(self):
        wd = self.app.wd
        x = int(wd.find_element_by_css_selector('span.quantity').get_attribute('innerText'))
        return x

    def return_to_main_page(self):
        wd = self.app.wd
        wait = self.wait
        wd.find_element_by_css_selector('li.general-0 a').click()
        # ожидание пока большая картинка пропадет #
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'a.main-image.fancybox.zoomable.shadow')))
        # ожидание пока обновится заголовок #
        wait.until(EC.title_is('Online Store | My Store'))
