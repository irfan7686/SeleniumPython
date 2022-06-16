from pageObjects.HomePage import HomePage
from utilities.BaseTest import BaseTest


class TestOne(BaseTest):
    def test_e2e(self):
        log = self.getLogger()
        log.info("Home Page Activity")
        log.info("Click on 'SHOP TAB' button on Homepage")
        homePage = HomePage(self.driver)
        log.info("Move to Product Page for ProductPage Activity")
        productPage = homePage.shopTab()
        log.info("Show all products on the Page")
        productTitleList = productPage.getProductTitles()
        log.info("Number of all the products on the page: " + str(len(productTitleList)))

        log.info("Iterate through all products on the page and add specific item to cart")
        i = -1
        for product in productTitleList:
            i = i + 1
            productName = product.text
            log.info("Product Names on the page: " + productName)
            if productName == "Blackberry":
                log.info("Selected Product: " + productName)
                log.info("click on Add product into cart")
                productPage.getProductAddBtn()[i].click()
                log.info(productName + " -product added into cart")

        log.info("Click on Checkout Button to go to Checkout Page and do CheckoutPage Activity")
        checkoutPage = productPage.toCheckoutPageBtn()
        log.info("Match selected product name is correct or not")
        assert "Blackberry" == checkoutPage.selectedProductName().text, "Selected product name is not as expected"
        log.info("Selected product name is as expected")

        log.info("Click on Checkout Button to go to ConfirmPage for ConfirmPage Activities")
        confirmPage = checkoutPage.checkoutButton()
        log.info("Enter CountryName to purchase the product")
        confirmPage.enterCountryName().send_keys("ind")

        log.info("Wait 10 secs for element to load")
        log.info("Verify if selected option is India")
        self.verifyElementPresence("India")

        # list of countries in dropdown
        countries = confirmPage.selectFromDropDown()
        for country in countries:
            if country.text == "India":
                country.click()
                break

        log.info("Selected Country: " + confirmPage.enterCountryName().get_attribute('value'))
        assert confirmPage.enterCountryName().get_attribute('value') == "India", "selected country is not India"

        log.info("Mark Check Agreement box")
        confirmPage.checkAgreement().click()

        log.info("Submit Purchase Order by clicking submit button")
        confirmPage.submit().click()

        succMsg = confirmPage.successMessage().text
        log.info(succMsg)
        log.info("Check if Substring is present in " + succMsg)
        assert "Success! Thank you!" in succMsg, "Substring is not present in Actual Success Message."
        log.info("Substring is present in " + succMsg)
