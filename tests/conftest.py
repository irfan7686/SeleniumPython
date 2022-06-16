import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    # parser.addoption("--headless", action="store", default="")
    parser.addoption("--url", action="store", default="Enter your Application URl here")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    print("Test setup execution")
    print("Setting Which Browser to complete the Test")
    browser_name = request.config.getoption("browser_name")
    # headless = request.config.getoption("headless")
    if browser_name == "chrome":
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--start-maximized")
        # chromeOptions.add_argument(headless)
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--ignore-certificate-errors")
        chromeOptions.add_argument("--ignore-ssl-errors")
        chromeOptions.add_argument("--ignore-certificate-errors-spki-list")
        driverPath = "C:\\1. Irfan_documents\\Softwares\\BrowserDrivers\\chromedriver.exe"
        # s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(executable_path=driverPath, options=chromeOptions)
    elif browser_name == "firefox":
        firefoxOptions = webdriver.FirefoxOptions()
        firefoxOptions.add_argument("--start-maximized")
        # firefoxOptions.add_argument(headless)
        firefoxOptions.add_argument("--disable-extensions")
        firefoxOptions.add_argument("--ignore-certificate-errors")
        firefoxOptions.add_argument("--ignore-ssl-errors")
        firefoxOptions.add_argument("--ignore-certificate-errors-spki-list")

        driverPath = "C:\\1. Irfan_documents\\Softwares\\BrowserDrivers\\geckodriver.exe"
        print("Selected Browser is 'Firefox'")
        driver = webdriver.Firefox(executable_path=driverPath, options=firefoxOptions)
    elif browser_name == "edge":
        edgeOptions = webdriver.EdgeOptions()
        edgeOptions.add_argument("--start-maximized")
        # edgeOptions.add_argument(headless)
        edgeOptions.add_argument("--disable-extensions")
        edgeOptions.add_argument("--ignore-certificate-errors")
        edgeOptions.add_argument("--ignore-ssl-errors")
        edgeOptions.add_argument("--ignore-certificate-errors-spki-list")
        driverPath = "C:\\1. Irfan_documents\\Softwares\\BrowserDrivers\\msedgedriver.exe"
        print("Selected Browser is 'Edge'")
        driver = webdriver.Edge(executable_path=driverPath, options=edgeOptions)
    else:
        print("Not a valid browser for testing")

    print("Selected Browser is: "+browser_name)
    # driver.maximize_window()
    applicationURL = request.config.getoption("url")
    driver.get(applicationURL)
    # driver.get("
    # ")

    # storing driver class object for further use in test class
    request.cls.driver = driver

    yield
    print("Closing Browser")
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            root_dir = "C:/Users/T951881/PycharmProjects/PythonSeleniumFramework/reports_n_logs/"
            file_name = "screenshot.png"
            # file_name = report.nodeid.replace("::", "_") + ".png"
            filePath = os.path.join(root_dir, file_name)
            print(filePath)
            _capture_screenshot(filePath)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


def pytest_html_report_title(report):
    report.title = "Python Selenium Report"