

#def test_list_len(app):
#    app.session.login_as_admin()
#    app.adm.get_list_len()

#def test_click_row_in_element(app):
#    app.session.login_as_admin()
#    app.adm.click_row_in_element('template')

def test_new(app):
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

