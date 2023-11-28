from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFoptions
import pytest
import os
import time


@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']

    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The 'BROWSER' environment variable must be set. "
                        "Use 'export BROWSER=chrome' (Linux/macOS) or 'set BROWSER=chrome' (Windows).")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported. "
                        f"Supported browsers are: {supported_browsers}")

    if browser in ('chrome', 'ch', 'headlesschrome'):
        chrome_options = webdriver.ChromeOptions()
        if browser == 'headlesschrome':
            chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser in ('firefox', 'ff'):
        # Add Firefox options if needed
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
    elif browser in ('headlesschrome'):
        chrome_options = ChOptions
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == 'headlessfirefox':
        ff_options = FFoptions()
        ff_options.add_argument("--disable-gpu")
        ff_options.add_argument("--no-sandbox")
        ff_options.add_argument("--headless")
        driver = webdriver.Firefox(options=ff_options)

    request.cls.driver = driver

    yield
    driver.quit()


