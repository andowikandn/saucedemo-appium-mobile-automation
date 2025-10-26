from appium.webdriver.common.appiumby import AppiumBy

class CheckoutLocator:
    checkout_page = (AppiumBy.XPATH, '//android.widget.TextView[@text="CHECKOUT: INFORMATION"]')
    first_name = (AppiumBy.ACCESSIBILITY_ID, 'test-First Name')
    last_name = (AppiumBy.ACCESSIBILITY_ID, 'test-Last Name')
    zip_code = (AppiumBy.ACCESSIBILITY_ID, 'test-Zip/Postal Code')
    continue_btn = (AppiumBy.ACCESSIBILITY_ID, 'test-CONTINUE')
    error_requirement_msg = (AppiumBy.ACCESSIBILITY_ID, 'test-Error message')
    checkout_firstname_required = (AppiumBy.XPATH, '//android.widget.TextView[@text="First Name is required"]')
    checkout_lastname_required = (AppiumBy.XPATH, '//android.widget.TextView[@text="Last Name is required"]')
    checkout_zipcode_required = (AppiumBy.XPATH, '//android.widget.TextView[@text="Postal Code is required"]')
    checkout_cancel_btn = (AppiumBy.ACCESSIBILITY_ID, 'test-CANCEL') 

class OverviewLocator:
    overview_page = (AppiumBy.XPATH, '//android.widget.TextView[@text="CHECKOUT: OVERVIEW"]')
    shipping_info = (AppiumBy.XPATH, '//android.widget.TextView[@text="Shipping Information:"]')
    payment_info = (AppiumBy.XPATH, '//android.widget.TextView[@text="Payment Information:"]')
    overview_cancel_btn = (AppiumBy.ACCESSIBILITY_ID, 'test-CANCEL')
    finish_btn = (AppiumBy.ACCESSIBILITY_ID, 'test-FINISH')

class CheckoutCompletedLocator:
    completed_page = (AppiumBy.XPATH, '//android.widget.TextView[@text="CHECKOUT: COMPLETE!"]')
    thank_you_for_order = (AppiumBy.XPATH, '//android.widget.TextView[@text="THANK YOU FOR YOU ORDER"]')
    back_home_btn = (AppiumBy.ACCESSIBILITY_ID, 'test-BACK HOME')