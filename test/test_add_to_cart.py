
'''
def test_add_to_cart_v01(app):
    wd = app.wd
    wd.get('http://localhost/litecart/public_html/en/')
    app.lt.add_product_to_cart()
    app.lt.add_product_to_cart()
    app.lt.add_product_to_cart()
    app.lt.add_product_to_cart()
    #app.lt.add_product_to_cart()
    #app.lt.add_product_to_cart()
    app.lt.remove_product_one_by_one()


def test_add_to_cart_new_v02(app):
    wd = app.wd
    wd.get('http://localhost/litecart/public_html/en/')
    app.lt.add_product_to_cart()
    app.lt.add_product_to_cart()
    app.lt.add_product_to_cart()
    #app.lt.add_product_to_cart()
    #app.lt.add_product_to_cart()
    #app.lt.add_product_to_cart()
    app.lt.remove_product_one_by_one_v01()
'''


def test_add_to_cart_new_v03(app):
    app.lt.open_page()
    app.lt.add_product_to_cart_v1()
    app.lt.add_product_to_cart_v1()
    app.lt.add_product_to_cart_v1()
    app.lt.remove_product_one_by_one_v02()

