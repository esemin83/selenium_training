

def test_login_as_admin(app):
    wd = app.wd
    wd.get("http://localhost/litecart/public_html/admin/")
    wd.find_element_by_name("username").send_keys('admin')
    wd.find_element_by_name("password").send_keys('admin')
    wd.find_element_by_css_selector("div.footer button").click()

