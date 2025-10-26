from pages.login import LoginPage
from pages.sort import SortPage
import allure

@allure.feature('4. Sorting product')
def test_sorting_products(driver):
    login = LoginPage(driver)
    sort = SortPage(driver)

    login.tap_autofill_standard_user()
    login.click_login()

    sort.sort_grid()
    sort.get_sort_grid()
    sort.sort_list()
    sort.get_sort_list()

    sort.tap_sort()
    sort.get_sort_item()
    sort.sort_by_price_hilo()
    sort.get_by_price_hilo()

    sort.tap_sort()
    sort.sort_by_price_lohi()
    sort.get_by_price_lohi()

    sort.tap_sort()
    sort.sort_by_name_za()
    sort.get_by_name_za()

    sort.tap_sort()
    sort.sort_by_name_az()
    sort.get_by_name_az()