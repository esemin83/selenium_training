

def test_click_all_new(app):
    app.session.login_as_admin()
    app.adm.click_appearence_new()
    app.adm.click_catalog_new()
    app.adm.click_countries_new()
    app.adm.click_currencies_new()
    app.adm.click_customers_new()
    app.adm.click_geo_zones_new()
    app.adm.click_languages_new()
    app.adm.click_modules_new()
    app.adm.click_orders_new()
    app.adm.click_pages_new()
    app.adm.click_reports_new()
    app.adm.click_setting_new()
    app.adm.click_slides_new()
    app.adm.click_tax_new()
    app.adm.click_translations_new()
    app.adm.click_users_new()
    app.adm.click_vqmods_new()
    app.session.logout_as_admin()

'''
def test_click_all(app):
    app.session.login_as_admin()

    app.adm.click_appearence()
    app.adm.click_catalog()
    app.adm.click_countries()
    app.adm.click_currencies()
    app.adm.click_customers()
    app.adm.click_geo_zones()
    app.adm.click_languages()
    app.adm.click_modules()
    app.adm.click_orders()
    app.adm.click_pages()
    app.adm.click_reports()
    app.adm.click_setting()
    app.adm.click_slides()
    app.adm.click_tax()
    app.adm.click_translations()
    app.adm.click_users()
    app.adm.click_vqmods()

    app.session.logout_as_admin()
'''