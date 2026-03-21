Feature: Cart functionality

  Background:
    Given user is logged in and item is added

  Scenario: Cart page opens successfully
    When user goes to cart
    Then cart page should load

  Scenario: Cart shows correct item count
    When user goes to cart
    Then cart should have 1 item

  Scenario: Remove item from cart
    When user goes to cart
    And user removes item from cart
    Then cart should be empty

  Scenario: Continue shopping from cart
    When user goes to cart
    And user clicks continue shopping
    Then user should be back on inventory page

  Scenario: Proceed to checkout from cart
    When user goes to cart
    And user clicks checkout
    Then user should be on checkout page