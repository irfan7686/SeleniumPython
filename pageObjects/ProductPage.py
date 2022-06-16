from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class ProductPage:

    # Class constructor for handling driver from actual test class
    def __init__(self, driver):
        self.driver = driver

    # Products Title locator
    # productsLocator = (By.CSS_SELECTOR, "h4[class='card-title']")
    productTitleLocator = (By.CSS_SELECTOR, ".card-title a")
    productAddBtnLocator = (By.CSS_SELECTOR, ".card-footer button")
    toCheckoutPageBtnLocator = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    # def productNameList(self):
    #     return self.driver.find_elements(*ProductPage.productsLocator)

    def getProductTitles(self):
        return self.driver.find_elements(*ProductPage.productTitleLocator)

    def getProductAddBtn(self):
        return self.driver.find_elements(*ProductPage.productAddBtnLocator)

    def toCheckoutPageBtn(self):
        self.driver.find_element(*ProductPage.toCheckoutPageBtnLocator).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
