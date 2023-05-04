from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
import pytest
import subprocess
from os import environ
import logging
from reportportal_client import RPLogger


@pytest.fixture(scope='function')
def driver(request):
    chrome_options = Chrome_Options()
    if request.config.getoption("headless") == "yes":
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = environ.get('CHROME_BINARY')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile': {
            'password_manager_enabled': False,
            'default_content_setting_values': {
                'notifications': 1
            }
        }
    })
    driver = webdriver.Chrome(executable_path=subprocess.getoutput('which chromedriver'), options=chrome_options)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default="no",
                     help='Headless is an option to run selenium with launched browser or not')


@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger

