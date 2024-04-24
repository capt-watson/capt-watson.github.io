from city_functions import name_city_functions


def test_city_country():
    answer = name_city_functions('valparaiso', 'chile', 'population = 1000000')
    assert answer == 'valparaiso chile - population = 1000000'
