*** Settings ***
Documentation     A test suite to test some features of provided webpage.
...
...               The workflow of this test is is created using keywords in
...               imported resource file below.
Library          ${CURDIR}/test_main.py

*** Variables ***
${PAGE_LINK}=    #Link Of The Website
${Browser}=    Chrome
${expected_Title}=    #Title of the Website
${grade_range}=    0

*** Tasks ***
Go To Site
    ${page}=  Test Initialize Page  ${PAGE_LINK}  ${Browser}
    Set Global Variable  ${page}

Validate Title
    ${title_same}=  Test Validate Title  ${page}  ${expected_Title}
    Should Be True  ${title_same}

Validate Grade Displayed And Has Value
    ${grade_present}  ${msg}=  Validate Grade  ${page}  ${grade_range}
    Should Be True  ${grade_present}  ${msg}

Validate The Info Icon
    ${icon_present}=  Validate Info Icon  ${page}
    Should Be True  ${icon_present}

Validate Review On The Page
    ${all_review_one}=  Validate Reviews  ${page}
    Should Be True  ${all_review_one}

Validate The Sum Of Percentage
    ${is_sum_as_expected}=  Calculate Percent Sum  ${page}
    Should Be True  ${is_sum_as_expected}

Quit Browser After Tests
    Close Window  ${page}
