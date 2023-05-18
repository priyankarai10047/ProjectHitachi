import requests
from behave import given, when, then, use_fixture


@given('A valid API URL "{endpoint}"')
def get_url(context, endpoint):
    context.url = endpoint


@when('User perform a GET with search query "{keyword}"')
def perfrom_get_operation(context, keyword):
    payload = {"s": keyword, "post_type": "page"}
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
    }
    context.response = requests.get(context.url, headers=header, params=payload)


@then("User should get a 200 response code")
def validate_response(context):
    assert context.response.status_code == 200
