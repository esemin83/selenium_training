

class Session:

    def __init__(self, app):
        self.app = app

    def login_as_admin(self):
        wd = self.app.wd
        wd.get("http://localhost/litecart/public_html/admin/")
        wd.find_element_by_name("username").send_keys("admin")
        wd.find_element_by_name("password").send_keys("admin")
        wd.find_element_by_css_selector("div.footer button").click()

    def logout_as_admin(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('a[href$="logout.php"]')

