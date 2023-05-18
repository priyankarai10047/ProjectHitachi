Feature: Users with correct URL should be able to navigate to Hitachi and invalid URL should be rejected

  Scenario: Users with correct URL should reach on Hitachi Home page
    Given Chrome browser has opened
    When User enters valid URL
    Then User navigation should be successful


  Scenario: User with wrong URL should get error
    Given Chrome browser has opened
    When User enters invalid URL
    Then User does not login to Hitachi website
