from countries import Countries


#def test_list_len(app):
#    app.session.login_as_admin()
#    app.adm.get_list_len()

#def test_click_row_in_element(app):
#    app.session.login_as_admin()
#    app.adm.click_row_in_element('template')

#def test_new(app):
#    app.session.login_as_admin()
#    app.adm.click_appearence_new()


def test_sadsasasd(app):
    app.session.login_as_admin()
    countries_list = app.adm.get_countries_list_v3()

    new_list = []
    for x in range(len(countries_list)):
        if countries_list[x][2] > 0:
            new_list.append(countries_list[x])

    print('\n', countries_list)
    print('\n', new_list)

    # [[38, 'Canada', 13], [223, 'United States', 65]]


def test_new(app):
    app.session.login_as_admin()
    l = app.adm.get_countries_list_on_country_page('Canada')
    l.remove("")
    print('\n', l)
    #print('\n', x)


def test_geo_zones(app):
    app.session.login_as_admin()
    countries_list = app.adm.get_countries_list_v3()

    list_with_geo_zones = []
    for x in range(len(countries_list)):
        if not countries_list[x][2] == 0:
            list_with_geo_zones.append(countries_list[x])

    print('\n' "countries_list =", countries_list)
    print('\n' "list_with_geo_zones =", list_with_geo_zones)

    for i in range(len(list_with_geo_zones)):
        cntry_list = app.adm.get_countries_list_on_country_page('%s' % list_with_geo_zones[i][1])
        cntry_list.remove("")
        print('\n' 'list of %s' % list_with_geo_zones[i][1], cntry_list)
        sorted_cntry_list = sorted(cntry_list)
        assert sorted_cntry_list == cntry_list
