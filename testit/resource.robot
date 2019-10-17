*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${SERVER}         34.69.218.188
${BROWSER}        Firefox
${DELAY}          0
${USER URL}      http://${SERVER}/v1/oppija/1
${ADMIN URL}     http://${SERVER}/v1/admin

*** Keywords ***
Open Browser To User Page
    Open Browser    ${USER URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    USer Page Should Be Open

Open Browser To Admin Page
    Open Browser    ${ADMIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Admin Page Should Be Open

Admin Page Should Be Open
    Location Should Be    ${ADMIN URL}
    Title Should Be    Admin

User Page Should Be Open
    Location Should Be    ${USER URL}
    Title Should Be   Oppija Sauko

Input Username
    [Arguments]    ${username}
    Input Text    username_field    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password_field    ${password}

Submit Credentials
    Click Button    login_button
