from behave import fixture
from selenium import webdriver

"""driver path for chrome Browser"""
CHROME_DRIVER_PATH = "D:/Automation/Webdriver/chromedriver.exe"


# -- FIXTURE- To pass Browser Driver to features
@fixture
def get_browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.close()
