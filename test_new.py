

def test_new(app):
    wd = app.wd
    wd.get("https://www.yandex.ru/")
    wd.find_element_by_css_selector("input#text").send_keys("find_to_find")
    wd.find_element_by_css_selector("div.search2__button button").click()





