 Feature: User should be able to search via API

  Scenario: User should be able to search via API
    Given A valid API URL "https://global.hitachi-solutions.com"
    When User perform a GET with search query "QA Automation"
    Then User should get a 200 response code
