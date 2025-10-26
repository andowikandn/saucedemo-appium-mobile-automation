from pages.login import LoginPage
import pytest
import allure

invalid_credentials = [
    ('', ''),
    ('standard_user', ''),
    ('', 'secret_sauce'),
    ('userwrong', 'passwrong')
]

@allure.feature('1. Login failed')
@pytest.mark.parametrize('x,y', invalid_credentials)
def test_login_failed(x,y,driver):
    login = LoginPage(driver)
    login.enter_username(x)
    login.enter_password(y)
    login.click_login()
    login.verify_login_failed()

@allure.feature('2. Login success')
def test_login_success(driver):
    login = LoginPage(driver)
    login.enter_username('standard_user')
    login.enter_password('secret_sauce')
    login.click_login()
    login.verify_login_success()

@allure.feature('3. Login autofill standard user')
def test_autofill_standard_user(driver):
    login = LoginPage(driver)
    login.tap_autofill_standard_user()
    login.click_login()