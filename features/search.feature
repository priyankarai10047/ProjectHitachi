Feature: User should be able to search valid keywords to Hitachi and successfully open the search result

Scenario: User wish to search should be able to successfully get search result
  Given Chrome Browser has opened
  When User enters valid URL
    And click on search button
    And Provides a valid keyword "QA Automation"
  Then Search result should be displayed

Scenario: Invalid keyword shows no result displayed
  Given Chrome Browser has opened
  When User enters valid URL
    And click on search button
    And Provides a invalid keyword "Priyanka"
  Then should get no result displayed


Scenario: User should be able to successfully open the search results
  Given Chrome Browser has opened
  When User enters valid URL
    And click on search button
    And Provides a valid keyword "QA Automation"
  Then Search result should be displayed
    And User should be able to click on them