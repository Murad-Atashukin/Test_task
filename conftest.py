import logging
import os
import pytest
from _pytest.fixtures import FixtureRequest
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.logging.logger import Logger
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper
from integrations.browsers.start import CustomStartup
from utils.json_utils import config


@pytest.fixture(scope="session", autouse=True)
def setup_session(request):

    work_dir = RootPathHelper.calling_root_path()
    os.chdir(work_dir)
    Logger.info(f'Setting work_dir: {work_dir}')

    for log_name in [
        "selenium.webdriver.remote.remote_connection",
        "selenium.webdriver.common.selenium_manager",
        "urllib3.connectionpool",
    ]:
        logger = logging.getLogger(log_name)
        logger.disabled = True

    Logger.info("Setup startup config")
    BrowserServices.Instance.set_startup(CustomStartup())
    yield


@pytest.fixture(scope="function", autouse=True)
def setup_function(request: FixtureRequest):
    browser = BrowserServices.Instance.browser
    browser.maximize()
    browser.go_to(config.start_url)
    browser.wait_for_page_to_load()
    yield
    if BrowserServices.Instance.is_browser_started:
        Logger.info("Closing browser")
        BrowserServices.Instance.browser.quit()
        BrowserServices.Instance.browser = None
