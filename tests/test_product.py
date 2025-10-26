from pages.product import ProductDetailPage, AddToCartsPage
from pages.login import LoginPage
import allure

@allure.feature('5. Product detail')
def test_product_details(driver):
    login = LoginPage(driver)
    products = ProductDetailPage(driver)

    login.tap_autofill_standard_user()
    login.click_login()
    products.tap_backpack_on_image()
    products.get_detail_backpack_image()
    products.tap_back_to_products()

    products.tap_backpack_on_text()
    products.get_detail_backpack_text()
    products.add_cart_backpack_in_detail()
    products.verify_add_cart_badge_backpack()
    products.remove_cart_badge()
    products.verify_remove_cart_badge_backpack()
    products.tap_back_to_products()

@allure.feature('6. Add to cart from dashboard')
def test_add_to_cart_products(driver):
    login = LoginPage(driver)
    addcart = AddToCartsPage(driver)

    login.tap_autofill_standard_user()
    login.click_login()
    addcart.add_to_carts_backpack_jacket()
    addcart.verify_add_carts_badge()
    addcart.remove_cart_backpack()
    addcart.verify_after_remove_cart_backpack()
    addcart.tap_cart_badge()
    addcart.verify_view_products_page()

@allure.feature('7. Continue shopping')
def test_add_cart_then_continue_shopping(driver):
    login = LoginPage(driver)
    addcart = AddToCartsPage(driver)
    product = ProductDetailPage(driver)

    login.enter_username('standard_user')
    login.enter_password('secret_sauce')
    login.click_login()

    addcart.add_to_cart_backpack_in_dashboard()
    addcart.tap_cart_badge()
    product.tap_continue_shopping()
    product.get_back_to_dashboard()