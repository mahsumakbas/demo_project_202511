from selenium.webdriver.common.by import By
import pytest
from time import sleep

link_practice_css = "li#menu-item-20>a"
link_practice_xpath = "//li[@id='menu-item-20']/a"

link_test_login_page_css = "div.post-content>div:nth-of-type(1) a"

practice_link_url = "https://practicetestautomation.com/practice/"
input_login_username = "#username"
input_login_password = "#password"
btn_form_submit = "button#submit"

logged_in_url ="https://practicetestautomation.com/logged-in-successfully/"
logged_in_page_title="Logged In Successfully | Practice Test Automation"
logged_in_text="Logged In Successfully"

text_post_title_css="h1.post-title"
btn_logout_css = "a.wp-block-button__link.has-text-color.has-background.has-very-dark-gray-background-color"
label_error = "div#error"


def test_success_login(setup_driver):

    setup_driver.find_element(By.CSS_SELECTOR, link_practice_css).click()
    assert setup_driver.current_url == practice_link_url, "Practice page URL is incorrect"
    setup_driver.find_element(By.CSS_SELECTOR, link_test_login_page_css).click()
    setup_driver.find_element(By.CSS_SELECTOR, input_login_username).send_keys("student")

    setup_driver.find_element(By.CSS_SELECTOR, input_login_password).send_keys("Password123")

    setup_driver.find_element(By.CSS_SELECTOR, btn_form_submit).click()
    sleep(1)

    assert setup_driver.current_url == logged_in_url, "Logged in page URL is incorrect"
    assert setup_driver.title == logged_in_page_title, "Login page title is incorrect"

    txt_logged_in = setup_driver.find_element(By.CSS_SELECTOR, text_post_title_css).text
    txt_logout = setup_driver.find_element(By.CSS_SELECTOR, btn_logout_css).text

    assert txt_logged_in == "Logged In Successfully", "Logged in page text is incorrect"
    assert txt_logout == "Log out", "Logout button text verification failed."

    

def test_failed_login_when_invalid_password(setup_driver):
    setup_driver.find_element(By.CSS_SELECTOR, link_practice_css).click()

    assert setup_driver.current_url == practice_link_url, "Practice page URL is incorrect"
    

    setup_driver.find_element(By.CSS_SELECTOR, link_test_login_page_css).click()

    setup_driver.find_element(By.CSS_SELECTOR, input_login_username).send_keys("student")
    sleep(2)
    setup_driver.find_element(By.CSS_SELECTOR, input_login_password).send_keys("invalidpass")
    sleep(2)
    setup_driver.find_element(By.CSS_SELECTOR, btn_form_submit).click()
    sleep(1)

    error_message = setup_driver.find_element(By.CSS_SELECTOR, label_error).text

    assert error_message == "Your password is invalid!", "Error message text is incorrect"




def test_failed_login_when_invalid_username(setup_driver):
    setup_driver.find_element(By.CSS_SELECTOR, link_practice_css).click()

    assert setup_driver.current_url == practice_link_url, "Practice page URL is incorrect"
    

    setup_driver.find_element(By.CSS_SELECTOR, link_test_login_page_css).click()

    setup_driver.find_element(By.CSS_SELECTOR, input_login_username).send_keys("nouser")
    sleep(2)
    setup_driver.find_element(By.CSS_SELECTOR, input_login_password).send_keys("invalidpass")
    sleep(2)
    setup_driver.find_element(By.CSS_SELECTOR, btn_form_submit).click()

    error_message = setup_driver.find_element(By.CSS_SELECTOR, label_error).text
    sleep(1)
    assert error_message == "Your username is invalid!", "Error message text is incorrect"