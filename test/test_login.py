

def test_login_as_admin(app):
    app.session.login_as_admin()
    app.session.logout_as_admin()

