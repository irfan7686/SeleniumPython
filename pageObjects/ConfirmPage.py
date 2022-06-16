from selenium.webdriver.common.by import By


class ConfirmPage:

    # Class constructor for handling driver from actual test class
    def __init__(self, driver):
        self.driver = driver

    # Locators on Confirm page
    enterCountryLocator = (By.CSS_SELECTOR, "input#country")
    ddCountriesLocator = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    agreementCBLocator = (By.CSS_SELECTOR, "div[class*='checkbox checkbox-primary']")
    submitBtnLocator = (By.XPATH, "//input[@type='submit']")
    succMsgLocator = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def enterCountryName(self):
        return self.driver.find_element(*ConfirmPage.enterCountryLocator)

    def selectFromDropDown(self):
        return self.driver.find_elements(*ConfirmPage.ddCountriesLocator)

    def checkAgreement(self):
        return self.driver.find_element(*ConfirmPage.agreementCBLocator)

    def submit(self):
        return self.driver.find_element(*ConfirmPage.submitBtnLocator)

    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.succMsgLocator)
