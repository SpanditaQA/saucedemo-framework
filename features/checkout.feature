Feature: Checkout functionality

  Background:
    Given user is logged in with item in cart and on checkout page

  Scenario: Complete checkout successfully
    When user fills valid checkout details
    And user clicks continue on checkout
    And user clicks finish
    Then order should be placed successfully

  Scenario: Checkout fails with missing first name
    When user fills checkout with missing first name
    And user clicks continue on checkout
    Then checkout error should be displayed

  Scenario: Checkout fails with missing last name
    When user fills checkout with missing last name
    And user clicks continue on checkout
    Then checkout error should be displayed

  Scenario: Checkout fails with missing postal code
    When user fills checkout with missing postal code
    And user clicks continue on checkout
    Then checkout error should be displayed

  Scenario: Cancel checkout goes back to cart
    When user cancels checkout
    Then user should be back on cart page