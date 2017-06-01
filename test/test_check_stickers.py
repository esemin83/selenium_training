def test_check_stickers(app):
    wd = app.wd
    wd.get('http://localhost/litecart/public_html/en/')
    # elements
    elements = wd.find_elements_by_css_selector('li.product.column.shadow.hover-light')
    for row in elements:
        l = []
        x = row.find_elements_by_css_selector("[class~=sticker]")
        l.append(x)
        assert len(l) == 1
        print('\n', l)


def test_check_stickers_new(app):
    wd = app.wd
    wd.get('http://localhost/litecart/public_html/en/')
    l = []
    n = 1
    for row in wd.find_elements_by_css_selector('li.product.column.shadow.hover-light'):
        sticker = row.find_element_by_css_selector("[class~=sticker]").get_attribute("title")
        l.append(sticker)
        assert len(l) == n
        n += 1
    assert len(l) == 11
    print('\n' "list =", l, '\n' "len list =", len(l), '\n' "n =", n)



