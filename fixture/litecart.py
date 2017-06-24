from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Litecart:

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(app.wd, 2)

    def create_new_user(self, first_name, last_name, email, password):
        wd = self.app.wd
        wd.get('http://localhost/litecart/public_html/en/')
        wd.find_element_by_css_selector('a[href$="create_account"]').click()
        # wd.find_element_by_name('tax_id').clear()
        # wd.find_element_by_name('tax_id').send_keys('123123')
        wd.find_element_by_name('firstname').clear()
        wd.find_element_by_name('firstname').send_keys('%s' % first_name)
        wd.find_element_by_name('lastname').clear()
        wd.find_element_by_name('lastname').send_keys('%s' % last_name)
        wd.find_element_by_name('address1').clear()
        wd.find_element_by_name('address1').send_keys('12345')
        wd.find_element_by_name('postcode').clear()
        wd.find_element_by_name('postcode').send_keys('12345')
        wd.find_element_by_name('city').clear()
        wd.find_element_by_name('city').send_keys('defoult')
        wd.find_element_by_name('email').clear()
        wd.find_element_by_name('email').send_keys('%s' % email)
        # выпадашка 1#

        #wd.find_element_by_css_selector('span.select2-selection__arrow').click()
        #wd.find_element_by_css_selector('input.select2-search__field').clear()
        #wd.find_element_by_css_selector('input.select2-search__field').send_keys('United States' + Keys.ENTER)

        # выпадашка 2 c select#
        select = Select(wd.find_element_by_css_selector('select.select2-hidden-accessible'))
        select.select_by_value('US')

        wd.find_element_by_name('phone').clear()
        wd.find_element_by_name('phone').send_keys('+72001001010')
        wd.find_element_by_name('password').clear()
        wd.find_element_by_name('password').send_keys('%s' % password)
        wd.find_element_by_name('confirmed_password').clear()
        wd.find_element_by_name('confirmed_password').send_keys('%s' % password)

        # checkbox check #
        checked = wd.find_element_by_name('newsletter').get_attribute("checked")
        print('checkbox old =', checked)
        if checked == 'true':
            wd.find_element_by_name('newsletter').click()  # .clear()
        checked_new = wd.find_element_by_name('newsletter').get_attribute("checked")
        print('checkbox new =', checked_new)
        # create #
        wd.find_element_by_name('confirmed_password').send_keys(Keys.TAB + Keys.ENTER)
        #print('!')

    def logout(self):
        wd = self.app.wd
        # return to home page #
        wd.find_element_by_css_selector('i.fa.fa-home').click()
        wd.find_element_by_css_selector('div.content a[href$="logout"]').click()

    def login(self, email, password):
        wd = self.app.wd
        wd.find_element_by_name('email').clear()
        wd.find_element_by_name('email').send_keys('%s' % email)
        wd.find_element_by_name('password').clear()
        wd.find_element_by_name('password').send_keys('%s' % password)
        wd.find_element_by_css_selector('span.button-set>button[name="login"]').click()

    def login_as(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('div.content a[href$="edit_account"]').click()
        user = wd.find_element_by_name('email').get_attribute("value")
        return user

######################################################################################################################
######################################################################################################################

    # Измененный сценарий работы с корзиной #

    def open_page(self):
        self.app.mp.mp_open()

    def add_product_to_cart_v1(self):
        # открыть первый продукт #
        self.app.mp.mp_open_first_product()
        # на случай выпадашки #
        if self.app.pp.select_is_present > 0:
            self.app.pp.click_select()
        # текущее значение счетчика в корзине #
        item_1 = self.app.pp.get_item_1
        # новое ожидаемое значение счетчика #
        new_value_of_item = item_1 + 1
        # нажать 'добавить' #
        self.app.pp.click_add(new_value_of_item)
        # новое значение счетчика в корзине #
        item_2 = self.app.pp.get_item_2
        # проверка, что значение соответствует ожидаемому #
        assert new_value_of_item == item_2
        self.app.pp.return_to_main_page()

    def remove_product_one_by_one_v02(self):
        # перейти в корзину #
        self.app.cp.cart_checkout()
        # всего эелементов в корзите #
        elements_in_table = self.app.cp.elements_in_table()
        # удалить #
        self.app.cp.remove(elements_in_table)
        # ожидание появления элемента '<< Back' #
        self.app.cp.is_finish()


######################################################################################################################

    def open_first_product(self):
        wd = self.app.wd
        wait = self.wait
        elements = wd.find_elements_by_css_selector('li.product.column.shadow.hover-light img')
        elements[0].click()
        # ожидание появления блока с информацией #
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tab-information")))

    def add_product_to_cart(self):
        wd = self.app.wd
        wait = self.wait
        # открыть первый продукт #
        self.open_first_product()
        # на случай выпадашки 1#
        '''
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select[name="options[Size]"]')))
            select = Select(wd.find_element_by_css_selector('select[name="options[Size]"]'))
            select.select_by_value('Small')
            print('Попалась выпадашка')
        except Exception:
            pass
        '''
        # на случай выпадашки 2 - работает куда бестрее#
        try:
            wd.find_element_by_css_selector('select[name="options[Size]"]')
            select = Select(wd.find_element_by_css_selector('select[name="options[Size]"]'))
            select.select_by_value('Small')
            print('\n', 'Попалась выпадашка')
        except Exception:
            pass

        # текущее значение счетчика в корзине #
        item_1 = int(wd.find_element_by_css_selector('span.quantity').get_attribute('innerText'))
        # новое ожидаемое значение счетчика #
        new_value_of_item = item_1 + 1

        # нажать 'добавить' #
        wd.find_element_by_css_selector('button[name="add_cart_product"]').click()
        # ожидание обновления счетчика в корзине #
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.quantity'), '%s' % new_value_of_item))

        # новое значение счетчика в корзине #
        item_2 = int(wd.find_element_by_css_selector('span.quantity').get_attribute('innerText'))
        # проверка, что значение соответствует ожидаемому #
        assert new_value_of_item == item_2
        self.return_to_main_page()
        print("\n" "item_old =", item_1, "\n" "item_new =", item_2)

    def return_to_main_page(self):
        wd = self.app.wd
        wait = self.wait
        wd.find_element_by_css_selector('li.general-0 a').click()
        # ожидание пока большая картинка пропадет #
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'a.main-image.fancybox.zoomable.shadow')))
        # ожидание пока обновится заголовок #
        wait.until(EC.title_is('Online Store | My Store'))

    def cart_checkout(self):
        wd = self.app.wd
        wait = self.wait
        wd.find_element_by_css_selector('a[href$="checkout"][class=link]').click()
        # ожидание появления кнопки 'удалить' #
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="remove_cart_item"]')))
        # ожидание пока обновится заголовок #
        wait.until(EC.title_is('Checkout | My Store'))

    def remove_product_one_by_one(self):
        wait = self.wait
        self.cart_checkout()
        # всего уток#
        count = self.count_in_table()
        # уток в поле ввода#
        current_value = self.current_value()
        print('в поле ввода =', current_value, 'всего =', count)
        for i in range(count):
            c = int(self.current_value())
            self.remove_one_duck_v2(c-1)
        # ожидание появления кнопки/ссылки 'Back' #
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-cart-wrapper a[href$="/public_html/en/"]')))

    def count_in_table(self):
        wd = self.app.wd
        l = []
        elements = wd.find_elements_by_css_selector(
            '#order_confirmation-wrapper tr:not([class="header"]):not([class="footer"]) td[style="text-align: center;"]')
        for row in elements:
            value = int(row.get_attribute('innerText'))
            l.append(value)
        count = sum(l)
        return count

    def current_value(self):
        wd = self.app.wd
        count = wd.find_element_by_css_selector('input[name="quantity"]').get_attribute('value')
        return count

    def remove_one_duck_v1(self, value):
        wd = self.app.wd
        wait = self.wait
        # ввести новое значение #
        wd.find_element_by_css_selector('input[name="quantity"]').click()
        wd.find_element_by_css_selector('input[name="quantity"]').clear()
        wd.find_element_by_css_selector('input[name="quantity"]').send_keys('%s' % value)
        # обновить значение #
        wd.find_element_by_css_selector('button[name="update_cart_item"]').click()
        # ожидание изменения таблицы #
        try:
            wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#order_confirmation-wrapper tr:not([class="header"]):not([class="footer"]) td[style="text-align: center;"]'), '%s' % value))
            print('Количество уток поубавилось')
        except Exception as txt:
            print('Одноцветные утки кончились, или исключение =', txt)

    def remove_one_duck_v2(self, value):
        wd = self.app.wd
        wait = self.wait
        # ввести новое значение #
        wd.find_element_by_css_selector('input[name="quantity"]').click()
        wd.find_element_by_css_selector('input[name="quantity"]').clear()
        wd.find_element_by_css_selector('input[name="quantity"]').send_keys('%s' % value)
        # первый элемент который пропадет после обновления #
        element = wd.find_element_by_css_selector(
            'tr:not([class="header"]):not([class="footer"]) td[style="text-align: center;"]')
        # обновить значение #
        wd.find_element_by_css_selector('button[name="update_cart_item"]').click()
        # ожидание изменения таблицы #
        try:
            wait.until(EC.staleness_of(element))
            print('Количество уток поубавилось')
        except Exception as txt:
            print('Одноцветные утки кончились, или исключение =', txt)

#######################################################################################################################

    def remove_product_one_by_one_v01(self):
        wd = self.app.wd
        wait = self.wait
        self.cart_checkout()
        # всего уток#
        elements_in_table = self.elements_in_table()
        print('elements =', elements_in_table, '\n', 'elements_len =', len(elements_in_table))
        for i in range(len(elements_in_table)):
            first_value_in_table = wd.find_element_by_css_selector(
                'tr:not([class="header"]):not([class="footer"]) td[style="text-align: center;"]')
            self.remove_product()
            try:
                # ожидание изменения первого элемента таблицы #
                wait.until(EC.staleness_of(first_value_in_table))
                print('Количество уток поубавилось')
            except Exception as txt:
                print('Исключение =', txt)
        # ожидание появления кнопки/ссылки 'Back' #
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-cart-wrapper a[href$="/public_html/en/"]')))

    def elements_in_table(self):
        wd = self.app.wd
        elements = wd.find_elements_by_css_selector('#order_confirmation-wrapper tr:not([class="header"]):not([class="footer"]) td[style="text-align: center;"]')
        l = []
        for row in elements:
            k = row
            l.append(k)
        return l

    def remove_product(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('button[name="remove_cart_item"]').click()



