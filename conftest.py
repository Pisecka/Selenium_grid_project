import os
import allure
import pytest
from selenium import webdriver
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
    parser.addoption("--executor", action="store", default="localhost")


@pytest.fixture(scope="session", autouse=True)
def get_environment(pytestconfig):
    props = {
        'Browser': 'Chrome',
        'Browser.Version': '99.0',
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

    if executor == "local":
        driver = driver_factory(browser)
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        # caps = {
        #     "browserName": browser,
        #     "browserVersion": b_version,
        #     "screenResolution": "1280x720",
        #     "name": "Karina",
        #     "selenoid:options": {
        #         "enableVNC": True,
        #         "enableVideo": False,
        #         #     "enableLog": logs
        #     },
        #     'acceptSslCerts': True,
        #     'acceptInsecureCerts': True,
        #     'timeZone': 'Europe/Moscow',
        #     'goog:chromeOptions': {}
        # }
        #if we want to write exactly which driver to use
        # options = Options()
        # driver = webdriver.Remote(
        #     command_executor=executor_url,
        #     options=webdriver.ChromeOptions()
        # )
        options = webdriver.ChromeOptions()
        options.set_capability("selenoid:options", {
                "enableVNC": True,
                "enableVideo": False,
            })
        options.set_capability("browserName", browser)
        options.set_capability("browserVersion", b_version)
        options.set_capability("screenResolution", "1280x720")
        options.set_capability("name", "Karina")
        options.set_capability("acceptSslCerts", True)
        options.set_capability("acceptInsecureCerts", True)
        options.set_capability("timeZone", "Europe/Moscow")

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )

    driver.url = url

    driver.t = 5

    driver.maximize_window()
    driver.get(url)
    request.addfinalizer(driver.quit)
    return driver
