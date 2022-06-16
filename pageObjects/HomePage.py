from selenium.webdriver.common.by import By

from pageObjects.ProductPage import ProductPage


class HomePage:

    # Class constructor for handling driver from actual test class
    def __init__(self, driver):
        self.driver = driver

    # Shop Button tab in Home page Locator
    shopBtnLocator = (By.CSS_SELECTOR, "a[href*='shop']")
    nameEditBoxLocator = (By.XPATH, "//div[@class='form-group']/input[@name='name']")
    emailEditBoxLocator = (By.CSS_SELECTOR, "input[name='email']")
    passwordEditBoxLocator = (By.XPATH, "//input[@id='exampleInputPassword1']")
    checkBoxLocator = (By.ID, "exampleCheck1")
    dropDownLocator = (By.ID, "exampleFormControlSelect1")
    radioLocator = (By.CSS_SELECTOR, "#inlineRadio2")
    birthdayEditboxLocator = (By.NAME, "bday")
    submitBtnLocator = (By.XPATH, "//input[@type='submit']")
    succMsgLocator = (By.XPATH, "//*[contains(@class,'alert-success')]")

    def shopTab(self):
        self.driver.find_element(*HomePage.shopBtnLocator).click()
        productPage = ProductPage(self.driver)
        return productPage
        # self.driver.find_element(by=By.CSS_SELECTOR, value="a[href*='shop']").click()

    def getName(self):
        return self.driver.find_element(*HomePage.nameEditBoxLocator)

    def getEmail(self):
        return self.driver.find_element(*HomePage.emailEditBoxLocator)

    def getPassword(self):
        return self.driver.find_element(*HomePage.passwordEditBoxLocator)

    def checkbox(self):
        return self.driver.find_element(*HomePage.checkBoxLocator)

    def selectGender(self):
        return self.driver.find_element(*HomePage.dropDownLocator)

    def selectEmployeeStatus(self):
        return self.driver.find_element(*HomePage.radioLocator)

    def getBirthDay(self):
        return self.driver.find_element(*HomePage.birthdayEditboxLocator)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submitBtnLocator)

    def successMessage(self):
        return self.driver.find_element(*HomePage.succMsgLocator)