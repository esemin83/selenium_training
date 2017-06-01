

def test_check_stickers_new(app):
    wd = app.wd
    wd.get('http://localhost/litecart/public_html/en/')
    # elements
    elements = wd.find_elements_by_css_selector('li.product.column.shadow.hover-light')
    for row in elements:
        l = []
        x1 = row.find_elements_by_css_selector("[class~=sticker]")
        l.append(x1)
        assert len(l) == 1



