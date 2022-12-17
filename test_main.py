from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import logging
import os



def test_initialize_page(link,browser):
    '''
    This function is to initialize the web browser. It takes two parameters:-
    link :- This is the link of the website you want to open.
    browser :- This is the browser in which you want to open the webpage.
    The function launches the web browser and access the link and then sends back the page object for further reference.
    '''
    pwd = os.getcwd()
    if str(browser) == 'Chrome':
        page = wb.Chrome(f'{pwd}/chromedriver')
    else:
        #please add the webdriver of the required browser
        page = wb.Chrome(f'{pwd}/chromedriver')
    page.set_window_size(1280,1080)
    page.get(link)
    logging.info('Opened browser with link')
    time.sleep(10)
    return page


def test_validate_title(page,expected_title):
    '''
    This function validates the title of the web page. It takes two parameters:-
    page :- The page object where the web page is open.
    expected_title :- The expected title of the webpage.
    The function gets the title of the webpage, compares it with the expected_title and sends back True if both matches
    or false
    '''
    actual_title = page.title.title()
    logging.info(expected_title)
    if actual_title.__contains__(expected_title):
        return True
    else:
        return False

def validate_grade(page,range):
    '''
    This function validates the total review displayed on the webpage. It takes two parameters:-
    page :- The page object where the web page is open.
    range :- The expected range above which the actual range should be displayed.
    The function verifies if the grade is dispalyed. If the grade is displayed it compares the value with expected
    range and sends back Tue/False accordingly with a message. If the grade is not displayed it sends back
    False with a message showing the error.
    '''
    range = int(range)
    grade_displayed = page.find_element(By.XPATH,"//span[@class='sc-677fb693-6 enOcMy']").is_displayed()
    if grade_displayed:
        actual_grade = page.find_element(By.XPATH,"//span[@class='sc-677fb693-6 enOcMy']").text
        if actual_grade.__contains__(','):
            actual_grade = actual_grade.split(',')
            int_grade = int(actual_grade[0])
        if int_grade >= range:
            msg = 'grade present and above the provided range'
            logging.info(f'Grade present on webpage with grade {int_grade}')
            return True,msg
        else:
            msg = 'grade present but less than range'
            logging.info(msg)
            return False, msg
    else:
        msg = 'Grade element not displayed'
        logging.info(msg)
        return False,msg

def validate_info_icon(page):
    '''
    This function validates the info icon of the web page. It takes one parameter:-
    page :- The page object where the web page is open.
    The function checks if the expected info icon is present and clickable. It then checks if the popup is being displayed
    as expected.
    It returns if popup is displayed else false otherwise.
    '''
    icon = page.find_element(By.XPATH,"//span[@class='Iconstyles__Icon-sc-hltmf-0 QNiDR cur-pointer hls hls-icon-feedback-info-circle-outline']")
    try:
        icon.click()
        popup = page.find_element(By.XPATH, "//div[@class='Modalstyles__Modal-sc-10yc67r-0 jtBvGW']").is_displayed()
        close_win = page.find_element(By.XPATH,"//span[@class='Iconstyles__Icon-sc-hltmf-0 bAWztQ Modalstyles__CloseIcon-sc-10yc67r-2 dsEOUn hls hls-icon-action-dismiss']")
        time.sleep(5)
        if close_win.is_displayed():
            close_win.click()
        if popup:
            logging.info('Icon present and is clickable')
            return True
        else:
            return False
    except WebDriverException:
        msg = 'The icon is not clickable'
        logging.debug(msg)


def validate_reviews(page):
    '''
    This function validates the title of the web page. It takes one parameter:-
    page :- The page object where the web page is open.
    The function verifies that when the reviews are filtered based on 1 star, then all the reviews displayed should
    have only one star.
    It returns true if only one star is present(has yellow color) or false if not.
    '''
    try:
        page.find_element(By.XPATH,"//a[@href='/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html?stars=1']").click()
        time.sleep(10)
        temp = page.find_elements(By.XPATH, "//div[@class='sc-dcf20c6c-0 sc-582e117-0 coLxdw hGgDCy']/div/div/div/span[@class='Iconstyles__Icon-sc-hltmf-0 czwZlJ  hls hls-star-filled']")
        len_revw = len(temp) #Number of star for each reviews in the first page
        res = 1
        itr = 0
        for i in range(len_revw):
            star_clr = temp[i].value_of_css_property('color')
            if itr == i and star_clr == 'rgba(255, 220, 15, 1)':
                res = res*1
                itr = itr +5
            elif itr != i and star_clr == 'rgba(204, 204, 204, 1)':
                res = res * 1
            else:
                res = res * 0
        if res == 1:
            logging.info('All the reviews in the page has 1 star')
            return True
        else:
            return False
    except WebDriverException:
        msg = 'The page element is not available'
        logging.debug(msg)


def calculate_percent_sum(page):
    '''
    This function validates the sum of total reviews diplayed on the website. It takes one parameter:-
    page :- The page object where the web page is open.
    The function gets the total number of percentages displayed on the website for all 5,4,3,2,1 star reviews.
    It gets the total of all the percentages and compare if it is less than or equal to 100.
    It returns True if sum is in the range or false otherwise.
    '''
    total = 0
    for i in range(1,6):
        percentage = page.find_element(By.XPATH,f"//a[@href='/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html?stars={i}']").text
        print(percentage)
        percentage = percentage.split('\n')
        percentage = percentage[1].split(' ')
        percentage = int(percentage[0])
        total = total + percentage
    logging.info(f'Total percentage of all reviews {total}')
    if total <= 100:
        return True
    else:
        return False


def close_window(page):
    '''
    This function quits the webpage which was open for testing. It takes one parameter:-
    page :- The page object where the web page is open.
    '''
    page.quit()



