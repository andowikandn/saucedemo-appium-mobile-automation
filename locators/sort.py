from appium.webdriver.common.appiumby import AppiumBy

class SortLocator:
    sort_list = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Toggle"]/android.widget.ImageView')
    sort_grid = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Toggle"]/android.widget.ImageView')
    tap_sort_by = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Modal Selector Button"]//android.widget.ImageView')
    sort_by_view = (AppiumBy.XPATH, '//android.widget.TextView[@text="Sort items by..."]')
    sort_by_cancel_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="Cancel"]')
    sort_by_price_hilo = (AppiumBy.XPATH, '//android.widget.TextView[@text="Price (high to low)"]')
    get_price_hilo_list = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="test-Price" and @text="$49.99"]')
    sort_by_price_lohi = (AppiumBy.XPATH, '//android.widget.TextView[@text="Price (low to high)"]')
    get_price_lohi_list = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="test-Price" and @text="$7.99"]')
    sort_by_name_za = (AppiumBy.XPATH, '//android.widget.TextView[@text="Name (Z to A)"]')
    get_name_za_list = (AppiumBy.XPATH, '//android.widget.TextView[@text="Test.allTheThings() T-Shirt (Red)"]')
    sort_by_name_az = (AppiumBy.XPATH, '//android.widget.TextView[@text="Name (A to Z)"]')
    get_name_az_list = (AppiumBy.XPATH, '//android.widget.TextView[@text="Sauce Labs Backpack"]')