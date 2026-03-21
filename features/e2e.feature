Feature: End to End user journey

  Scenario: User completes full shopping flow
    Given user opens the saucedemo website
    When user logs in with valid credentials
    Then user should land on inventory page
    When user sorts products by price low to high
    And user adds first product to cart
    Then cart badge should show count as "1"
    When user goes to the cart page
    Then cart should contain 1 item
    When user removes the item from cart
    Then cart should be empty now