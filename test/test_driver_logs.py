

def test_driver_logs(app):
    wd = app.wd

    app.session.login_as_admin()
    app.adm.open_product_list()
    app.adm.click_products()

    for q in wd.get_log('browser'):
        print(q)
