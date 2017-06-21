from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
import string
import random
import os.path
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_re():
    x = 'rgba(119, 119, 119, 1)'
    y = clear(x)
    z = search(y)
    print(z, z[0], z[1], z[2])


def clear(s):
        return re.sub("[() \s \ rgb \ rgba]", "", s)


def search(y):
    return re.split('\,', y)


def test_random_name_new():
    name_1 = random_val('mail', 15)
    name_2 = random_val('name', 15)
    print(name_1, name_2)


def random_val(pref, maxlen):
    value = string.ascii_letters + string.digits
    generated = "".join([random.choice(value) for x in range(random.randrange(maxlen))])
    if pref == 'mail':
        result = 'a' + generated + '@ru'
    elif pref == 'name':
        result = 'a' + generated
    return result


def test_where_are_you(app):
    wd = app.wd
    wd.get('http://localhost/litecart/public_html/en/')
    wd.find_element_by_css_selector('a[href$="create_account"]').click()
    element = wd.find_element_by_css_selector('table button[type="submit"]')#.size
    location = element.location
    size = element.size
    ActionChains(wd).move_by_offset('30', '705').click().perform()
    print(location, size)


def test_get_l(app):
    app.session.login_as_admin()
    l = app.adm.get_product_list()
    #k = l.index('aC')
    try:
        l.index('aaC')
        print('in list')
    except ValueError:
        print('not in list')

    #assert l.index('aC') is not None
    print(l)


def test_driver_logs():
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities=d)
    # load some site
    driver.get('http://foo.com')
    # print messages
    for entry in driver.get_log('browser'):
        print(entry)
