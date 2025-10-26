from locators.checkout import CheckoutLocator, OverviewLocator, CheckoutCompletedLocator
from locators.dashboard import DashboardLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import allure

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def verify_checkout_page(self):
        with allure.step('Verify checkout page'):
            assert self.wait.until(
                EC.presence_of_element_located(CheckoutLocator.checkout_page)).is_displayed()

    def enter_requirement_firstname(self, firstname: str):
        with allure.step('Input first name field'):
            self.wait.until(
                EC.presence_of_element_located(CheckoutLocator.first_name)).send_keys(firstname)
        
    def enter_requirement_lastname(self, lastname: str):
        with allure.step('Input last name field'):
            self.wait.until(
                EC.presence_of_element_located(CheckoutLocator.last_name)).send_keys(lastname)
    
    def enter_requirement_zipcode(self, zipcode: str):
        with allure.step('Input zipcode field'):
            self.wait.until(
                EC.presence_of_element_located(CheckoutLocator.zip_code)).send_keys(zipcode)
            
    def tap_continue_btn(self):
        with allure.step('User tap continue button'):
            self.wait.until(
                EC.element_to_be_clickable(CheckoutLocator.continue_btn)).click()
            
    def verify_requirement_error_message(self):
        with allure.step('Verify error message requirement field'):
            assert self.wait.until(
                EC.presence_of_element_located(CheckoutLocator.error_requirement_msg)).is_displayed()
        
class OverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def verify_overview_page(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollBackward().scrollIntoView(new UiSelector().text("Shipping Information:"))'
        ) # scroll down
        sleep(0.5)
        with allure.step('Verify overview page'):
            assert self.wait.until(
                EC.presence_of_element_located(OverviewLocator.overview_page)).is_displayed()

            assert self.wait.until(
                EC.presence_of_element_located(OverviewLocator.payment_info)).is_displayed()
            
            assert self.wait.until(
                EC.presence_of_element_located(OverviewLocator.shipping_info)).is_displayed()
        
    def tap_finish_btn(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
            'new UiSelector().text("FINISH"))'
        ) # scroll down to tap
        sleep(0.5)

        with allure.step('User tap finish button'):
            self.wait.until(
                EC.visibility_of_element_located(OverviewLocator.finish_btn)).click()
        
class CheckoutCompletedPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def verify_checkout_completed_page(self):
        with allure.step('Verify checkout completed page'):
            assert self.wait.until(
                EC.presence_of_element_located(CheckoutCompletedLocator.completed_page)).is_displayed()
            
            assert self.wait.until(
                EC.presence_of_element_located(CheckoutCompletedLocator.thank_you_for_order)).is_displayed()
        sleep(0.5)
        
    def tap_back_home(self):
        with allure.step('User tap back home button'):
            self.wait.until(
                EC.element_to_be_clickable(CheckoutCompletedLocator.back_home_btn)).click()
            
            assert self.wait.until(
                EC.presence_of_element_located(DashboardLocator.dashboard_page)).is_displayed()