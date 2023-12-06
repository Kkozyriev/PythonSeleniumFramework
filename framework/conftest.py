from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFoptions
import pytest
import os
import pytest_html


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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        xfail = hasattr(report, "wasxfail")
        # check if test failed
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = True if 'init_driver' in item.fixturenames else False
            if is_frontend_test:
                results_dir = os.environ.get("RESULT_DIR")
                if not results_dir:
                    raise Exception("Environment variable 'RESULT_DIR' must be set.")
                screenshot_path = os.path.join(results_dir, item.name + '.png')
                driver_fixture = item.funcargs['request']
                driver_fixture.cls.driver.save_screenshot(screenshot_path)


                # only add additional html on failure
                extras.append(pytest_html.extras.image(screenshot_path))

        report.extras = extras

