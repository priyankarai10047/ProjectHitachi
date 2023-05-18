from behave import when, then
from pages.HomePage import HomePage
from pages.SearchResultPage import SearchResultPage

# Constants for our assertions
EXPECTED_TEXT_FOR_VALID_SEARCH_RESULT = "Search results for: QA Automation"
EXPECTED_TEXT_FOR_INVALID_SEARCH_RESULT = (
    "Sorry, your search didn't return any results."
)
EXPECTED_TEXT_FOR_CLICKABLE_RESULT = "Retail Supply Chain"


@when("click on search button")
def expand_search_area(context):
    context.homePage = HomePage(context.driver)
    context.homePage.search_click()


@when('Provides a valid keyword "{keyword}"')
def provides_search_text(context, keyword):
    context.homePage.search_keyword(keyword)


@then("Search result should be displayed")
def verify_search_results(context):
    context.search_result_page = SearchResultPage(context.driver)
    value = context.search_result_page.result_displayed()
    assert value == EXPECTED_TEXT_FOR_VALID_SEARCH_RESULT


@when('Provides a invalid keyword "{keyword}"')
def perform_invalid_search(context, keyword):
    context.homePage.search_keyword(keyword)


@then("should get no result displayed")
def verify_no_results_found(context):
    context.search_result_page = SearchResultPage(context.driver)
    invalid_value = context.search_result_page.result_displayed()
    assert invalid_value == EXPECTED_TEXT_FOR_INVALID_SEARCH_RESULT


@then("User should be able to click on them")
def verify_results_clickable(context):
    actual_text = context.search_result_page.option_selection()
    assert actual_text == EXPECTED_TEXT_FOR_CLICKABLE_RESULT
