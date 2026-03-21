Feature: Login functionality

  Scenario: Valid login
    Given user is on login page
    When user logs in with valid credentials
    Then user should land on inventory page

  Scenario: Invalid login
    Given user is on login page
    When user logs in with invalid credentials
    Then user should see error message

  Scenario: Blank username
    Given user is on login page
    When user logs in with blank username
    Then user should see error message

  Scenario: Blank password
    Given user is on login page
    When user logs in with blank password
    Then user should see error message

  Scenario: Locked out user
    Given user is on login page
    When locked out user tries to login
    Then user should see locked error message

  Scenario Outline: Login with multiple users
    Given user is on login page
    When user logs in as "<username>" with password "<password>"
    Then user should land on inventory page

    Examples:
      | username                | password     |
      | standard_user           | secret_sauce |
      | performance_glitch_user | secret_sauce |