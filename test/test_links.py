

def test_links(app):
    app.session.login_as_admin()
    app.adm.click_countries_new()
    app.adm.create_new_country()
    app.adm.click_links()
