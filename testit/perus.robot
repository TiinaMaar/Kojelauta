*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

*** Test Cases ***
Valid Enter Student User
    Open Browser To User Page
    User Page Should Be Open
    [Teardown]    Close Browser

Valid Enter Admin
    Open Browser To Admin Page
    Admin Page Should Be Open
    [Teardown]    Close Browser

Alter Schedule
    Open Browser To Admin Page
    Admin Page Should Be Open
    [Teardown]    Close Browser
    

