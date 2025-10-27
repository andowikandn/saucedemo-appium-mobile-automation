from locators.sidebar import SidebarMenuLocator
from locators.login import LoginLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class SidebarMenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def tap_sidebar_menu(self):
        with allure.step('User tap sidebar menu'):
            self.wait.until(
                EC.element_to_be_clickable(SidebarMenuLocator.burger_menu)).click()
        
    def view_sidebar_menu(self):
        with allure.step('Verify view sidebar menu'):
            assert self.wait.until(
                EC.presence_of_element_located(SidebarMenuLocator.all_items)).is_displayed()
            
    def tap_close_sidebar_menu(self):
        with allure.step('User tap close sidebar menu'):
            self.wait.until(
                EC.element_to_be_clickable(SidebarMenuLocator.close_burger)).click()
        
    def tap_webview_menu(self):
        with allure.step('User tap webview menu'):
            self.wait.until(
                EC.element_to_be_clickable(SidebarMenuLocator.webview_menu)).click()
            
    def webview_search_bing_url(self, search: str):
        with allure.step('User input bing url: wwww.bing.com'):
            self.wait.until(
                EC.presence_of_element_located(SidebarMenuLocator.webview_input_url)).send_keys(search)
        
    def tap_goto_site_btn(self):
        with allure.step('User tap goto site button'):
            self.wait.until(
                EC.presence_of_element_located(SidebarMenuLocator.webview_goto_site)).click()
            
    def verify_bing_url(self):
        with allure.step('Verify bing url: www.bing.com'):
            logo_bing = self.wait.until(
                EC.presence_of_element_located(SidebarMenuLocator.logo_bing))
            assert logo_bing.is_displayed()
            return logo_bing.text
            
class LogoutMenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def tap_logout_menu(self):
        with allure.step('User tap logout menu'):
            self.wait.until(
                EC.element_to_be_clickable(SidebarMenuLocator.logout_menu)).click()
        
    def verify_logout(self):
        with allure.step('Verify has success logout'):
            assert self.wait.until(
                EC.presence_of_element_located(LoginLocator.login_page)
                ).is_displayed()
