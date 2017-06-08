from test.test_create_new_user import random_val


def test_create_new_product(app):
    app.session.login_as_admin()
    product_name = random_val('name', 10)
    file_name = 'lenin.jpg'
    app.adm.create_product(product_name, file_name)
    l = app.adm.get_product_list()
    try:
        l.index(product_name)
        print('Product in list')
        result = 'True'
    except ValueError:
        print('Product not in list')
        result = 'False'
    assert result == 'True'

