from pages.login import LoginPage
from pages.product import ProductDetailPage, AddToCartsPage
from pages.checkout import CheckoutPage, OverviewPage, CheckoutCompletedPage
import pytest
import allure

checkout_requirement_field = [
    ('','',''),
    ('Abdul','',''),
    ('Abdul','Malik','')
]

@pytest.mark.parametrize('x,y,z', checkout_requirement_field)
@allure.feature('8. Checkout requirement field error message')
def test_checkout_requirement_field(x,y,z,driver):
    login = LoginPage(driver)
    addcart = AddToCartsPage(driver)
    product = ProductDetailPage(driver)
    checkout = CheckoutPage(driver)

    login.tap_autofill_standard_user()
    login.click_login()
    addcart.add_to_cart_backpack_in_dashboard()
    addcart.tap_cart_badge()
    product.tap_checkout_btn()

    checkout.verify_checkout_page()
    checkout.enter_requirement_firstname(x)
    checkout.enter_requirement_lastname(y)
    checkout.enter_requirement_zipcode(z)
    checkout.tap_continue_btn()
    checkout.verify_requirement_error_message()
    
@allure.feature('9. Checkout end to end')
def test_checkout_E2E(driver):
    login = LoginPage(driver)
    addcart = AddToCartsPage(driver)
    product = ProductDetailPage(driver)
    checkout = CheckoutPage(driver)
    overview = OverviewPage(driver)
    completed = CheckoutCompletedPage(driver)

    login.tap_autofill_standard_user()
    login.click_login()
    addcart.add_to_carts_backpack_jacket()
    addcart.tap_cart_badge()
    product.scroll_checkout_btn()
    product.tap_checkout_btn()

    checkout.enter_requirement_firstname('Budi')
    checkout.enter_requirement_lastname('Pekerti')
    checkout.enter_requirement_zipcode('12345')
    checkout.tap_continue_btn()
    
    overview.verify_overview_page()
    overview.tap_finish_btn()

    completed.verify_checkout_completed_page()
    completed.tap_back_home()