Feature: login feature

  @firstTestScenario
  Scenario Outline: Login to quora and check that logged in successfully
    Given goto <url> microsite and login with <emailid> and <password>

    Examples:
      | url                                      | emailid              | password    |
      | kelloggsfamilyrewards.pdn.retaileriq.com | mmomaya@quotient.com | Testing_123 |