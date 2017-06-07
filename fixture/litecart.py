from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Litecart:

    def __init__(self, app):
        self.app = app

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
        # выпадашка #
        wd.find_element_by_css_selector('span.select2-selection__arrow').click()
        wd.find_element_by_css_selector('input.select2-search__field').clear()
        wd.find_element_by_css_selector('input.select2-search__field').send_keys('United States' + Keys.ENTER)

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
