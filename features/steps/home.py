from behave import given, when, then, use_fixture
from webdriver_fixture import get_browser

EXPECTED_TITLE_FOR_VALID_URL = "Home – Hitachi Solutions"
VALID_URL = "https://global.hitachi-solutions.com/"
INVALID_URL = "https://www.facebook.com/"


@given("Chrome browser has opened")
def get_chrome_browser(context):
    context.driver = use_fixture(get_browser, context)


@when("User enters valid URL")
def open_valid_url(context):
    context.driver.get(VALID_URL)


@then("User navigation should be successful")
def verify_homepage_opened(context):
    assert context.driver.title == EXPECTED_TITLE_FOR_VALID_URL


@when("User enters invalid URL")
def open_invalid_url(context):
    context.driver.get(INVALID_URL)


@then("User does not login to Hitachi website")
def verify_homepage_not_opened(context):
    assert context.driver.title != EXPECTED_TITLE_FOR_VALID_URL
