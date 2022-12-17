This project is used to verify testcases on the https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html
webpage.
The project covers the below testcases:
1.Check if the page title exists
2.Check if the grade is visible and is above zero (e.g. 4.81/5.00)
3.Hover over the info icon of the first review in the list ((i) on to right) - ensure that the popup window appears
4.Click on "1 Stern" to filter all "one star" reviews - ensure that every review in the list has only one star
5.Create the sum of all star percentage values. The sum must be equal or below 100.

To run the testcases, install the required packages from requirements.txt and follow the below steps.

1. Install Python 3.9.6 and pip 21.3.1 in your environment.
2. Setup the environment by installing the required packages by running the following command in the terminal -> pip install -r requirements.txt
3. Download the required webdriver if browser other than chrome is required and add in the project. Current version of chromedriver present in the project is for Chrome Version 108.0.5359.94
4. Provide the link of the website to be tested in the UI_TestCases.robot file under the variables section.
5. Provide the be tested in the UI_TestCases.robot file under the variables section.
6. Open the terminal and goto project working directory.
7. Run the following command in the terminal -> robot test_full.robot
8. After the test completes, verify the result on report.html