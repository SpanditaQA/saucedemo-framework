Feature: Inventory page functionality

  Background:
    Given user is logged in

  Scenario: Products are displayed on inventory page
    Then user should see products on the page

  Scenario: Product count is correct
    Then user should see 6 products

  Scenario: Sort products by price low to high
    When user sorts products by "lohi"
    Then products should be sorted successfully

  Scenario: Sort products by name Z to A
    When user sorts products by "za"
    Then products should be sorted successfully

  Scenario: Add first product to cart
    When user adds first product to cart
    Then cart badge should show "1"