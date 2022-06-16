from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    # Class constructor for handling driver from actual test class
    def __init__(self, driver):
        self.driver = driver

    # Locators on checkout page
    selectedProductNameLocator = (By.XPATH, "//a[contains(text(),'Blackberry')]")
    checkoutBtnLocator = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def selectedProductName(self):
        return self.driver.find_element(*CheckoutPage.selectedProductNameLocator)

    def checkoutButton(self):
        self.driver.find_element(*CheckoutPage.checkoutBtnLocator).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
