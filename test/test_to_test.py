import re


def test_re():
    x = 'rgba(119, 119, 119, 1)'
    y = clear(x)
    z = search(y)
    print(z, z[0], z[1], z[2])


def clear(s):
        return re.sub("[() \s \ rgb \ rgba]", "", s)


def search(y):
    return re.split('\,', y)
