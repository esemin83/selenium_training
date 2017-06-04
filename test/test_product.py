import string
#box-campaigns li.product.column.shadow.hover-light strong.campaign-price

def test_product(app):
    wd = app.wd
    # data on main page
    wd.get('http://localhost/litecart/public_html/en/')
    name = wd.find_element_by_css_selector('#box-campaigns li.product.column.shadow.hover-light div.name').get_attribute("textContent")
    regular_price = wd.find_element_by_css_selector(
        '#box-campaigns li.product.column.shadow.hover-light s.regular-price').get_attribute("textContent")
    campaign_price = wd.find_element_by_css_selector(
        '#box-campaigns li.product.column.shadow.hover-light strong.campaign-price').get_attribute("textContent")
    regular_price_color = wd.find_element_by_css_selector(
        '#box-campaigns li.product.column.shadow.hover-light s.regular-price').value_of_css_property("color")
    regular_price_size = wd.find_element_by_css_selector(
        '#box-campaigns li.product.column.shadow.hover-light s.regular-price').size
    campaign_price_color = wd.find_element_by_css_selector(
        '#box-campaigns li.product.column.shadow.hover-light strong.campaign-price').value_of_css_property("color")
    campaign_price_size = wd.find_element_by_css_selector(
        '#box-campaigns li.product.column.shadow.hover-light strong.campaign-price').size

    value_on_main_page = []
    value_on_main_page.append([name, regular_price, campaign_price])

    # regular_price_color
    c1 = int(regular_price_color[4:7])
    c2 = int(regular_price_color[9:12])
    c3 = int(regular_price_color[14:17])

    # color = grey
    assert c1 == c2 == c3

    # campaign_price_color
    c4 = int(campaign_price_color[4:7])
    c5 = int(campaign_price_color[9:10])
    c6 = int(campaign_price_color[12:13])

    # color = red
    assert c4 != 0 and c5 == 0 and c6 == 0

    # size of elements
    sr1 = int(regular_price_size['height'])
    sr2 = int(regular_price_size['width'])
    sc1 = int(campaign_price_size['height'])
    sc2 = int(campaign_price_size['width'])

    assert sr1 <= sc1 and sr2 <= sc2

    # data on product page
    wd.find_element_by_css_selector('#box-campaigns li.product.column.shadow.hover-light').click()
    name_p = wd.find_element_by_css_selector('h1').get_attribute("textContent")
    regular_price_p = wd.find_element_by_css_selector('s.regular-price').get_attribute("textContent")
    campaign_price_p = wd.find_element_by_css_selector('strong.campaign-price').get_attribute("textContent")

    value_on_product_page = []
    value_on_product_page.append([name_p, regular_price_p, campaign_price_p])

    assert value_on_main_page == value_on_product_page

    print("\n", "value_on_main_page =", value_on_main_page)
    print("value_on_product_page =", value_on_product_page)
    print("regular_price_color =", regular_price_color)
    print("c1=", c1, "c2=", c2, "c3=", c3)
    print("campaign_price_color =", campaign_price_color)
    print("c4=", c4, "c5=", c5, "c6=", c6)
    print("regular_price_size=", regular_price_size)
    print("sr1=", sr1, "sr2=", sr2)
    print("campaign_price_size=", campaign_price_size)
    print("sc1=", sc1, "sc2=", sc2)
