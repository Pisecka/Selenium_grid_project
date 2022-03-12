import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


DRIVERS = os.path.expanduser("~/Documents/drivers")


def driver_factory(browser):
    if browser == "chrome":
        service = Service(executable_path=os.path.join(DRIVERS, "chromedriver"))
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = Service(executable_path=os.path.join(DRIVERS, "geckodriver"))
        driver = webdriver.Firefox(service=service)
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=os.path.join(DRIVERS, "operadriver"))
    elif browser == "edge":
        service = Service(executable_path=os.path.join(DRIVERS, "msedgedriver"))
        driver = webdriver.Edge(service=service)
    else:
        raise Exception("Driver not supported")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://demo.opencart.com/")


@pytest.fixture
def browser(request):
    driver = driver_factory(request.config.getoption("--browser"))
    url = request.config.getoption("--url")
    driver.url = url
    driver.t = 5

    driver.maximize_window()
    driver.get(url)
    request.addfinalizer(driver.quit)
    return driver