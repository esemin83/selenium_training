import re


def clear(s):
    return re.sub("[() \s \ rgb \ rgba]", "", s)


def search(y):
    return re.split('\,', y)


def test_product(app):
    wd = app.wd
    # data on main page #
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

    # regular_price_color main page #
    rbg_rp = clear(regular_price_color)
    rbg_rp_list = search(rbg_rp)

    c1 = int(rbg_rp_list[0])
    c2 = int(rbg_rp_list[1])
    c3 = int(rbg_rp_list[2])

    # ASSERT COLOR = GREY MAIN PAGE#
    assert c1 == c2 == c3

    # campaign_price_color main page #
    rbg_cp = clear(campaign_price_color)
    rbg_cp_list = search(rbg_cp)

    c4 = int(rbg_cp_list[0])
    c5 = int(rbg_cp_list[1])
    c6 = int(rbg_cp_list[2])

    # ASSERT COLOR = RED MAIN PAGE#
    assert c4 != 0 and c5 == 0 and c6 == 0

    # size of elements main page #
    sr1 = int(regular_price_size['height'])
    sr2 = int(regular_price_size['width'])
    sc1 = int(campaign_price_size['height'])
    sc2 = int(campaign_price_size['width'])

    # ASSERT SIZE MAIN PAGE#
    assert sr1 <= sc1 and sr2 <= sc2

    # data on product page #
    wd.find_element_by_css_selector('#box-campaigns li.product.column.shadow.hover-light').click()
    name_p = wd.find_element_by_css_selector('h1').get_attribute("textContent")
    regular_price_prod_page = wd.find_element_by_css_selector('s.regular-price').get_attribute("textContent")
    campaign_price_prod_page = wd.find_element_by_css_selector('strong.campaign-price').get_attribute("textContent")
    regular_price_prod_page_color = wd.find_element_by_css_selector('s.regular-price').value_of_css_property("color")
    regular_price_prod_page_size = wd.find_element_by_css_selector('s.regular-price').size
    campaign_price_prod_page_color = wd.find_element_by_css_selector('strong.campaign-price').value_of_css_property("color")
    campaign_price_prod_page_size = wd.find_element_by_css_selector('strong.campaign-price').size


    value_on_product_page = []
    value_on_product_page.append([name_p, regular_price_prod_page, campaign_price_prod_page])

    # ASSERT VALUES ON MAIN AND PRODUCT PAGE #

    assert value_on_main_page == value_on_product_page

    # regular_price_prod_page_color #
    rbg_rp_prod = clear(regular_price_prod_page_color)
    rbg_rp_list_prod = search(rbg_rp_prod)

    a1 = int(rbg_rp_list_prod[0])
    a2 = int(rbg_rp_list_prod[1])
    a3 = int(rbg_rp_list_prod[2])

    # ASSERT COLOR = GREY PRODUCT PAGE#
    assert a1 == a2 == a3

    # campaign_price_prod_page_color #
    rbg_cp_prod = clear(campaign_price_prod_page_color)
    rbg_cp_list_prod = search(rbg_cp_prod)

    q4 = int(rbg_cp_list_prod[0])
    q5 = int(rbg_cp_list_prod[1])
    q6 = int(rbg_cp_list_prod[2])

    # ASSERT COLOR = RED PRODUCT PAGE#
    assert q4 != 0 and q5 == 0 and q6 == 0

    # size of elements product page #
    tt1 = int(regular_price_prod_page_size['height'])
    tt2 = int(regular_price_prod_page_size['width'])
    bb1 = int(campaign_price_prod_page_size['height'])
    bb2 = int(campaign_price_prod_page_size['width'])

    # ASSERT SIZE PRODUCT PAGE#
    assert tt1 <= bb1 and tt2 <= bb2

    print("value_on_main_page =", value_on_main_page)
    print("value_on_product_page =", value_on_product_page)
    print("regular_price_color main page =", rbg_rp_list)
    print("campaign_price_color main page =", rbg_cp_list)
    print("regular_price_size main page =", regular_price_size)
    print("campaign_price_size main page =", campaign_price_size)
    print("regular_price_prod_page_color main page =", regular_price_prod_page_color, rbg_rp_list_prod)
    print("regular_price_prod_page_size =", regular_price_prod_page_size)
    print("campaign_price_prod_page_color =", campaign_price_prod_page_color, rbg_cp_list_prod)
    print("campaign_price_prod_page_size =", campaign_price_prod_page_size)
