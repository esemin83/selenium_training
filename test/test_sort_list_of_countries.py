

def test_sort_countries_on_main_page(app):
    app.session.login_as_admin()
    countries_list = app.adm.get_countries_list_v3()
    only_country_list = []
    for x in range(len(countries_list)):
        only_country_list.append(countries_list[x][1])
    sorted_only_country_list = sorted(only_country_list)
    assert sorted_only_country_list == only_country_list
    print('\n', countries_list)
    print('\n', only_country_list)
    print('\n', sorted_only_country_list)


def test_sort_countries_on_country_page(app):
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
