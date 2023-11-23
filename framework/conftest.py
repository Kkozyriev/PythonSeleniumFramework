from selenium import webdriver
import pytest
import os

@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff']

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

    request.cls.driver = driver
    yield
    driver.quit()
