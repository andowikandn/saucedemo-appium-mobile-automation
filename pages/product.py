from locators.dashboard import DashboardLocator
from locators.product import ViewProductLocator
from locators.dashboard import DashboardLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import allure

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
    
    def tap_backpack_on_image(self):
        with allure.step('User tap backpack on image'):
            self.wait.until(
                EC.element_to_be_clickable(DashboardLocator.tap_product_img_backpack)).click()
        
    def get_detail_backpack_image(self):
        with allure.step('Verify detail product backpack based on image'):
            assert self.wait.until(
                EC.presence_of_element_located(ViewProductLocator.view_product_backpack_on_img)).is_displayed()

    def tap_backpack_on_text(self):
        with allure.step('User tap backpack on text'):
            self.wait.until(
                EC.element_to_be_clickable(DashboardLocator.tap_product_txt_backpack)).click()

    def get_detail_backpack_text(self):
        with allure.step('Verify detail product backpack based on text'):
            assert self.wait.until(
                EC.visibility_of_element_located(ViewProductLocator.view_product_backpack_on_txt)).is_displayed()

    def add_cart_backpack_in_detail(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollBackward().scrollIntoView(new UiSelector().text("ADD TO CART"))'
        ) # scroll down
        sleep(0.5)
        with allure.step('Add to cart backpack from product detail page'):
            self.wait.until(
                EC.element_to_be_clickable(ViewProductLocator.add_cart_backpack_in_detail)).click()

    def verify_add_cart_badge_backpack(self):
        with allure.step('Verify cart badge after add product'):
            assert self.wait.until(
                EC.presence_of_element_located(ViewProductLocator.view_add_cart_badge)).is_displayed()

    def remove_cart_badge(self):
        with allure.step('User tap remove button'):
            self.wait.until(
                EC.element_to_be_clickable(ViewProductLocator.remove_cart_badge)).click()

    def verify_remove_cart_badge_backpack(self):
        with allure.step('Verify cart badge after remove product'):
            assert self.wait.until(
                EC.presence_of_element_located(ViewProductLocator.view_remove_cart_badge)).is_displayed()

    def tap_back_to_products(self):
        with allure.step('User tap back to product button'):
            self.wait.until(
                EC.element_to_be_clickable(ViewProductLocator.back_to_product_btn)).click()

    def get_back_to_dashboard(self):
        with allure.step('Verify get back to dashboard'):
            assert self.wait.until(
                EC.presence_of_element_located(DashboardLocator.dashboard_page)).is_displayed()

    def tap_continue_shopping(self):
        with allure.step('User tap continue shopping button'):
            self.wait.until(
                EC.element_to_be_clickable(ViewProductLocator.continue_shopping_btn)).click()

    def tap_checkout_btn(self):
        with allure.step('User tap checkout button'):
            self.wait.until(
                EC.element_to_be_clickable(ViewProductLocator.checkout_btn)).click()
            
    def scroll_checkout_btn(self):
        with allure.step('Scroll to checkout button'):
            self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollBackward().scrollIntoView(new UiSelector().text("CHECKOUT"))'
        ) # scroll down
        sleep(0.5)


class AddToCartsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart_backpack_in_dashboard(self):
        with allure.step('Add to cart backpack from dashboard'):
            self.wait.until(
                EC.presence_of_element_located(DashboardLocator.add_to_cart_backpack_in_dashboard)).click()
    
    def add_to_carts_backpack_jacket(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollBackward().scrollIntoView(new UiSelector().text("$49.99"))'
        ) # scroll down
        sleep(0.5)
        with allure.step('Add to cart jacket from dashboard'):
            add_cart_jacket = self.wait.until(
                EC.visibility_of_element_located(DashboardLocator.add_to_cart_jacket))
            add_cart_jacket.click()

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollForward().scrollIntoView(new UiSelector().text("$29.99"))'
        ) # scroll up
        sleep(0.5)
        with allure.step('Add to cart backpack from dashboard'):
            add_cart_backpack = self.wait.until(
                EC.visibility_of_element_located(DashboardLocator.add_to_cart_backpack_in_dashboard))
            add_cart_backpack.click()

    def verify_add_carts_badge(self):
        with allure.step('Verify cart badge after add cart product backpack'):
            assert self.wait.until(
                EC.presence_of_element_located(DashboardLocator.view_add_carts_badge)).is_displayed()

    def remove_cart_backpack(self):
        with allure.step('User tap remove button product backpack'):
            self.wait.until(
                EC.element_to_be_clickable(DashboardLocator.remove_cart_backpack)).click()

    def verify_after_remove_cart_backpack(self):
        with allure.step('Verify cart badge after remove cart product backpack'):
            assert self.wait.until(
                EC.presence_of_element_located(DashboardLocator.view_remove_cart_badge)).is_displayed()

    def tap_cart_badge(self):
        with allure.step('User tap cart badge'):
            self.wait.until(
                EC.element_to_be_clickable(DashboardLocator.cart_badge)).click()
    
    def verify_view_products_page(self):
        with allure.step('Verify your cart product page'):
            assert self.wait.until(
                EC.presence_of_element_located(ViewProductLocator.your_cart_page)).is_displayed()