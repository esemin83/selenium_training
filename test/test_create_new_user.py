import string
import random


def random_val(pref, maxlen):
    value = string.ascii_letters + string.digits
    generated = "".join([random.choice(value) for x in range(random.randrange(maxlen))])
    if pref == 'mail':
        result = 'a' + generated + '@ru'
    elif pref == 'name':
        result = 'a' + generated
    return result


def test_create_new_user(app):
    wd = app.wd
    wd.get('http://localhost/litecart/public_html/en/')
    first_name = random_val('name', 10)
    last_name = random_val('name', 10)
    email = random_val('mail', 10)
    password = 'test'
    app.lt.create_new_user(first_name, last_name, email, password)
    app.lt.logout()
    app.lt.login(email, password)
    user = app.lt.login_as()
    app.lt.logout()
    assert user.upper() == email.upper()
    print('user =', user, user.upper(), email.upper())

'''
def test_login_logout(app):
    wd = app.wd
    wd.get('http://localhost/litecart/public_html/en/')
    app.lt.login('fake_5@ru', 'test')
    user = app.lt.login_as()
    app.lt.logout()
    print('user =', user)
'''