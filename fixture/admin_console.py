import os.path
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Admin_console:

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(app.wd, 5)

    def click_appearence(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="template"]').click()
        assert "Template | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="logotype"]').click()
        assert "Logotype | My Store" in wd.title

    def click_catalog(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="catalog"]').click()
        assert "Catalog | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="product_groups"]').click()
        assert "Product Groups | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="option_groups"]').click()
        assert "Option Groups | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="manufacturers"]>span').click()
        assert "Manufacturers | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="suppliers"]>span').click()
        assert "Suppliers | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="delivery_statuses"]>span').click()
        assert "Delivery Statuses | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="sold_out_statuses"]>span').click()
        assert "Sold Out Statuses | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="quantity_units"]>span').click()
        assert "Quantity Units | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="csv"]>span').click()
        assert "CSV Import/Export | My Store" in wd.title

    def click_countries(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="countries"]').click()
        assert "Countries | My Store" in wd.title

    def click_currencies(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="currencies"]').click()
        assert "Currencies | My Store" in wd.title

    def click_customers(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="customers"]').click()
        assert "Customers | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="csv"]>span').click()
        assert "CSV Import/Export | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="newsletter"]>span').click()
        assert "Newsletter | My Store" in wd.title

    def click_geo_zones(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="geo_zones"]').click()
        assert "Geo Zones | My Store" in wd.title

    def click_languages(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="languages"]').click()
        assert "Languages | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="storage_encoding"]>span').click()
        assert "Storage Encoding | My Store" in wd.title

    def click_modules(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="jobs"]').click()
        assert "Job Modules | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="customer"]>span').click()
        assert "Customer Modules | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="shipping"]>span').click()
        assert "Shipping Modules | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="payment"]>span').click()
        assert "Payment Modules | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="order_total"]>span').click()
        assert "Order Total Modules | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="order_action"]>span').click()
        assert "Order Action Modules | My Store" in wd.title

    def click_orders(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="orders"]').click()
        assert "Orders | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="order_statuses"]>span').click()
        assert "Order Statuses | My Store" in wd.title

    def click_pages(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="pages"]').click()
        assert "Pages | My Store" in wd.title

    def click_reports(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="monthly_sales"]').click()
        assert "Monthly Sales | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="most_sold_products"]>span').click()
        assert "Most Sold Products | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="most_shopping_customers"]>span').click()
        assert "Most Shopping Customers | My Store" in wd.title

    def click_setting(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="store_info"]').click()
        assert "Settings | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="defaults"]>span').click()
        assert "Settings | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="general"]>span').click()
        assert "Settings | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="listings"]>span').click()
        assert "Settings | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="images"]>span').click()
        assert "Settings | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="checkout"]>span').click()
        assert "Settings | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="advanced"]>span').click()
        assert "Settings | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="security"]>span').click()
        assert "Settings | My Store" in wd.title

    def click_slides(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="slides"]').click()
        assert "Slides | My Store" in wd.title

    def click_tax(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="tax_classes"]').click()
        assert "Tax Classes | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="tax_rates"]>span').click()
        assert "Tax Rates | My Store" in wd.title

    def click_translations(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="translations&doc=search"]').click()
        assert "Search Translations | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="scan"]>span').click()
        assert "Scan Files For Translations | My Store" in wd.title
        wd.find_element_by_css_selector('a[href$="translations&doc=csv"]>span').click()
        assert "CSV Import/Export | My Store" in wd.title

    def click_users(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="users"]').click()
        assert "Users | My Store" in wd.title

    def click_vqmods(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="vqmods"]').click()
        assert "vQmods | My Store" in wd.title
######################################################################################################################
######################################################################################################################

    def get_list_len(self, name):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="%s"]' % name).click()
        elements = wd.find_elements_by_css_selector('li[id|="doc"]')
        l = []
        for row in elements:
            x = row.find_elements_by_css_selector('span.name')
            l.append(x)
        n = len(l)
        return n

    def click_row_in_element(self, name):
        wd = self.app.wd
        n = self.get_list_len(name)
        for x in range(n):
            wd.find_elements_by_css_selector('li[id|="doc"] a[href^="http:"]')[x].click()
        print("\n" "%s len=" % name, n)

    def click_appearence_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="template"]').click()
        assert "Template | My Store" in wd.title
        self.click_row_in_element('template')

    def click_catalog_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="catalog"]').click()
        assert "Catalog | My Store" in wd.title
        self.click_row_in_element('catalog')

    def click_countries_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="countries"]').click()
        assert "Countries | My Store" in wd.title

    def click_currencies_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="currencies"]').click()
        assert "Currencies | My Store" in wd.title

    def click_customers_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="customers"]').click()
        assert "Customers | My Store" in wd.title
        self.click_row_in_element('customers')

    def click_geo_zones_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="geo_zones"]').click()
        assert "Geo Zones | My Store" in wd.title

    def click_languages_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="languages"]').click()
        assert "Languages | My Store" in wd.title
        self.click_row_in_element('languages')

    def click_modules_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="jobs"]').click()
        assert "Job Modules | My Store" in wd.title
        self.click_row_in_element('jobs')

    def click_orders_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="orders"]').click()
        assert "Orders | My Store" in wd.title
        self.click_row_in_element('orders')

    def click_pages_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="pages"]').click()
        assert "Pages | My Store" in wd.title

    def click_reports_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="monthly_sales"]').click()
        assert "Monthly Sales | My Store" in wd.title
        self.click_row_in_element('monthly_sales')

    def click_setting_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="store_info"]').click()
        assert "Settings | My Store" in wd.title
        self.click_row_in_element('store_info')

    def click_slides_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="slides"]').click()
        assert "Slides | My Store" in wd.title

    def click_tax_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="tax_classes"]').click()
        assert "Tax Classes | My Store" in wd.title
        self.click_row_in_element('tax_classes')

    def click_translations_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="translations&doc=search"]').click()
        assert "Search Translations | My Store" in wd.title
        self.click_row_in_element('translations&doc=search')

    def click_users_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="users"]').click()
        assert "Users | My Store" in wd.title

    def click_vqmods_new(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="vqmods"]').click()
        assert "vQmods | My Store" in wd.title

######################################################################################################################
######################################################################################################################

    def get_countries_list_v3(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="countries"]').click()
        elements = wd.find_elements_by_css_selector('tr.row')
        l = []
        for row in elements:
            id = row.find_element_by_css_selector('tr.row td:nth-child(3)').get_attribute("textContent")
            name = row.find_element_by_css_selector('tr.row td:nth-child(5)').get_attribute("textContent")
            geo_zones = row.find_element_by_css_selector('tr.row td:nth-child(6)').get_attribute("textContent")
            l.append([int(id), name, int(geo_zones)])
        return l

    def get_countries_list_on_country_page(self, name):
        wd = self.app.wd
        #wd.find_element_by_css_selector('li#app->a[href$="countries"]').click()
        wd.find_element_by_link_text('%s' % name).click()
        elements = wd.find_elements_by_css_selector('#table-zones td:nth-child(3)')
        l = []
        for row in elements:
            name = row.find_element_by_css_selector('#table-zones td:nth-child(3) input').get_attribute("value")
            l.append(name)
        return l

######################################################################################################################
######################################################################################################################

    def create_product(self, product_name, file_name):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="catalog"]').click()
        assert "Catalog | My Store" in wd.title

        # GENERAL #
        wd.find_element_by_css_selector('a[href$="edit_product"]').click()
        wd.find_element_by_name('name[en]').send_keys('%s' % product_name)
        wd.find_element_by_name('code').send_keys('321')
        wd.find_element_by_name('quantity').send_keys(Keys.DELETE + '32')

        # path #
        file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', file_name))
        wd.find_element_by_css_selector('input[name="new_images[]"]').send_keys(file)

        # for chrome only #
        wd.find_element_by_name('date_valid_from').send_keys('08-06-2017')
        wd.find_element_by_name('date_valid_to').send_keys('08-06-2018')

        # PRICES #
        time.sleep(1)
        wd.find_element_by_css_selector('a[href="#tab-prices"]').click()
        wd.find_element_by_name('purchase_price').send_keys(Keys.DELETE + '13')

        # выпадашка select#
        select = Select(wd.find_element_by_css_selector('select[name="purchase_price_currency_code"]'))
        select.select_by_value('EUR')

        # хитрое поле#
        wd.find_element_by_name('gross_prices[USD]').send_keys(Keys.LEFT_CONTROL + 'a' +
                                                               Keys.LEFT_CONTROL + Keys.DELETE + '3')
        # submit #
        wd.find_element_by_css_selector('button[name = "save"]').click()

        f = open('screen.jpg', 'w')
        wd.get_screenshot_as_file('screen.jpg')
        f.close()
        #print('!')

    def get_product_list(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('li#app->a[href$="catalog"]').click()
        # a[href*="product_id"]:not([title="Edit"])
        l = []
        elements = wd.find_elements_by_css_selector('tr.row.semi-transparent')#:not([title="Edit"])')
        for row in elements:
            product_name = row.find_element_by_css_selector('a[href*="product_id"]:not([title="Edit"])')\
                .get_attribute("innerText")
            l.append(product_name)
        return l

######################################################################################################################

    def create_new_country(self):
        wd = self.app.wd
        wait = self.wait
        wd.find_element_by_css_selector('a[href$="edit_country"]').click()
        wait.until(EC.presence_of_element_located((By.NAME, 'iso_code_2')))

    def get_main_window_id(self):
        wd = self.app.wd
        l = wd.window_handles
        x = l[0]
        return x

    def get_new_window_id(self, main_window):
        wd = self.app.wd
        l = wd.window_handles
        l.remove(main_window)
        return l

    def click_links(self):
        wd = self.app.wd
        wait = self.wait

        main_window = self.get_main_window_id()
        print('\n' 'main_window =', main_window)

        elements = wd.find_elements_by_css_selector('i.fa.fa-external-link')

        for i in range(len(elements)):
            elements[i].click()
            new_id = self.get_new_window_id(main_window)
            wd.switch_to.window(new_id[0])
            wait.until(EC.new_window_is_opened(new_id))
            k = wd.title
            wd.close()
            wd.switch_to.window(main_window)
            print('i =', i, 'title is=', k)

######################################################################################################################

    def open_product_list(self):
        wd = self.app.wd
        wait = self.wait
        wd.find_element_by_css_selector('li#app->a[href$="catalog"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href$="category_id=0"]')))
        wd.find_element_by_css_selector('a[href$="category_id=1"]').click()
        #print('!')

    def get_product_list_on_catalog(self):
        wd = self.app.wd
        elements = wd.find_elements_by_css_selector('a[href*="category_id="]:nth-child(2):not([class="button"])')
        l = []
        for row in elements:
            n = row.get_attribute('innerHTML')
            l.append(n)
        return l

    def click_products(self):
        wd = self.app.wd
        t = self.get_product_list_on_catalog()
        for i in range(len(t)):
            wd.find_element_by_link_text('%s' % t[i]).click()
            self.open_product_list()





