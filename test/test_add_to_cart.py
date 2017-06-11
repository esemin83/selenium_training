

def test_add_to_cart(app):
    wd = app.wd
    wd.get('http://localhost/litecart/public_html/en/')
    app.lt.add_product_to_cart()
    app.lt.add_product_to_cart()
    app.lt.add_product_to_cart()
    app.lt.add_product_to_cart()
    #app.lt.add_product_to_cart()
    #app.lt.add_product_to_cart()
    app.lt.remove_product_one_by_one()

