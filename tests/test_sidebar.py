from pages.sidebar import SidebarMenuPage, LogoutMenuPage
from pages.login import LoginPage
import allure

@allure.feature('10. Sidebar and webview menu user search url')
def test_view_sidebar_menu(driver):
    login = LoginPage(driver)
    sidebar = SidebarMenuPage(driver)

    login.enter_username('standard_user')
    login.enter_password('secret_sauce')
    login.click_login()

    sidebar.tap_sidebar_menu()
    sidebar.view_sidebar_menu()
    sidebar.tap_close_sidebar_menu()

    sidebar.tap_sidebar_menu()
    sidebar.tap_webview_menu()
    sidebar.webview_search_bing_url('www.bing.com')
    sidebar.tap_goto_site_btn()
    sidebar.verify_bing_url()

@allure.feature('11. User do logout menu')
def test_logout_menu(driver):
    login = LoginPage(driver)
    sidebar = SidebarMenuPage(driver)
    logout = LogoutMenuPage(driver)

    login.enter_username('standard_user')
    login.enter_password('secret_sauce')
    login.click_login()

    sidebar.tap_sidebar_menu()
    logout.tap_logout_menu()
    logout.verify_logout()