Feature: pet operations
    
    Scenario: get pet by id
        when make get request with id 1
        then response code is 200

    Scenario: create a pet
        when make request to create a pet with name Alice
        then response code is 200


    Scenario Outline: get username
        when make request to get user <username>
        then response code is <response_code>

        Examples: Amphibians
        | username          | response_code |
        | deneme            | 404          |
        | username          | 200           |
        | mahsum            | 404   |
        | another-user      | 404     |
