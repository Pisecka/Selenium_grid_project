import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
allure

def driver_factory(browser):
    if browser == "chrome":
        driver = webdriver.ChromeOptions()
    elif browser == "firefox":
        driver = webdriver.FirefoxOptions()
    else:
        raise Exception("Driver not supported")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--b_version", default="117.0")
    parser.addoption("--url", default="https://demo.opencart.com/")
    parser.addoption("--executor", action="store", default="http://192.168.0.3:4444")


@pytest.fixture(scope="session", autouse=True)
def get_environment(pytestconfig):
    props = {
        'Browser': 'Chrome',
        'Browser.Version': '117.0',
        'Shell': os.getenv('SHELL')
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/allure-report/environment.properties', 'w') as f:
        env_props = '\n'.join([f'{k}={v}' for k, v in props.items()])
        f.write(env_props)


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    b_version = request.config.getoption("--b_version")
    executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")

    if executor == "http://192.168.0.3:4444/wd/hub":
        driver = driver_factory(browser)
    else:
        executor_url = f"http://192.168.0.3:4444/wd/hub"
        caps = {
            "browserName": browser,
            "browserVersion": b_version,
            "screenResolution": "1280x720",
            "name": "Karina",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False,
                #     "enableLog": logs
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            'goog:chromeOptions': {}
        }
        #if we want to write exactly which driver to use
        # options = Options()
        # driver = webdriver.Remote(
        #     command_executor=executor_url,
        #     options=webdriver.ChromeOptions()
        # )

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=driver_factory(browser)
        )

    driver.url = url

    driver.t = 5

    driver.maximize_window()
    driver.get(url)
    request.addfinalizer(driver.quit)
    return driver
