*** Settings ***
Resource    resource.robot
Test Setup  Create User  testuser  testpassword123

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User
    Input Credentials  newvaliduser  NewValidPass123!
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User
    Input Credentials  kalle  AnotherValid123!
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command And Create User
    Input Credentials  ab  ValidPass123!
    Output Should Contain  Error: Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input New Command And Create User
    Input Credentials  user!@#  ValidPass123!
    Output Should Contain  Error: Invalid username

Register With Valid Username And Too Short Password
    Input New Command And Create User
    Input Credentials  validboi  a
    Output Should Contain  Error: Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Create User
    Input Credentials  validboii  asdasdasdsadsda
    Output Should Contain  Error: Password cannot contain only letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123