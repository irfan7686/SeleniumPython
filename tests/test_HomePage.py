import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseTest import BaseTest


class TestHomePage(BaseTest):
    def test_UserRegistration(self, getData):
        log = self.getLogger()
        try:
            log.info("Home Page Activity")
            homePage = HomePage(self.driver)
            log.info("Enter all details to register new user")
            log.info("Enter Name in editbox")
            homePage.getName().send_keys(getData["fName"])
            log.info("Enter Email in editbox")
            homePage.getEmail().send_keys(getData["email"])
            log.info("Enter Password in editbox")
            homePage.getPassword().send_keys(getData["password"])
            log.info("Select checkbox")
            homePage.checkbox().click()
            log.info("Select gender from dropdown list")
            self.selectDDOptionsByText(homePage.selectGender(), getData["gender"])
            log.info("Select Employment status")
            homePage.selectEmployeeStatus().click()
            log.info("Enter DOB")
            homePage.getBirthDay().send_keys(getData["dob"])
            log.info("Submit the form")
            homePage.submitForm().click()
            log.info("Check success message after form submission")
            message = homePage.successMessage().text
            assert "Success!" in message, "'Success!' is not present in displayed Success String"
            log.info("'Success!' is present in " + message)
            self.refreshBrowser()
        except Exception as e:
            log.info("Test Failed due to: " + str(e))

        finally:
            log.info("TestCase execution is complete.")

    # Reading data for parameterizing the same test for n number of iterations
    # @pytest.fixture(params=HomePageData.test_HomePageData)
    # Reading data from Excel file and iterate for number rows
    @pytest.fixture(params=BaseTest.getTestDataSetAllRows(BaseTest.testDataPath, "HomePageDataSheet"))
    # Reading data from Excel file based on testcaseId
    # @pytest.fixture(params=BaseTest.getTestDataByID(BaseTest.testDataPath, "HomePageDataSheet", "TC2"))
    def getData(self, request):
        return request.param
