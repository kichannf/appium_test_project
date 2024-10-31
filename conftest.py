import allure
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver import Remote
from dotenv import load_dotenv

from src.pages.auth_page import AuthPage
from src.pages.user_page import UserPage

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.habitrpg.android.habitica',
    appActivity='.ui.activities.MainActivity',
    waitForIdleTimeout=0,
    app='C:\\kichan\dev\\appiumTestProject\\src\\app\\Habitica_4.3.3_apkcombo.com.apk'
)

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

appium_server_url = 'http://localhost:4723'


@pytest.fixture(autouse=True, scope='session')
def load_env():
    load_dotenv()

@pytest.fixture()
def driver():
    web_driver = webdriver.Remote(
        appium_server_url,
        options=capabilities_options)
    yield web_driver
    if web_driver:
        web_driver.quit()


@pytest.fixture()
def start_page(driver: Remote):
    yield AuthPage(driver)


@pytest.fixture()
def user_page(start_page):
    with allure.step('Авторизация'):
        page = start_page \
            .skip_onboarding_by_skip_btn() \
            .open_login_form() \
            .login()
        yield UserPage(page.driver)


@pytest.fixture()
def authed_page(driver: Remote):
    yield driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
        driver = item.funcargs.get('driver')
        if driver:
            allure.attach(
                body=driver.get_screenshot_as_png(),
                name=f"exception_screenshot",
                attachment_type=allure.attachment_type.PNG)
    else:
        item.status = 'passed'
