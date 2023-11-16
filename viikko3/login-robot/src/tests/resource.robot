*** Settings ***
Library  ../AppLibrary.py
Resource    resource.robot

*** Keywords ***
Input Login Command
    Input  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

Input New Command
    Input  new

Create User
    [Arguments]  ${username}  ${password}
    AppLibrary.Create User  ${username}  ${password}