

class Admin_console:

    def __init__(self, app):
        self.app = app

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
        wd.find_element_by_css_selector('li#app->a[href$="countries"]').click()
        wd.find_element_by_link_text('%s' % name).click()
        elements = wd.find_elements_by_css_selector('#table-zones td:nth-child(3)')
        l = []
        for row in elements:
            name = row.find_element_by_css_selector('#table-zones td:nth-child(3) input').get_attribute("value")
            l.append(name)
        return l
