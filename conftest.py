from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="session", autouse=True)
def before_session():
    print("This runs before the test session starts")
    yield
    print("This runs after the test session ends")


@pytest.fixture(scope="function")
def setup_driver():

    #driver = webdriver.Chrome()

    print("this is before each test case")
    options = webdriver.ChromeOptions()
    
    driver = webdriver.Remote(
        command_executor='http://http://host.docker.internal:4444/wd/hub',
        options=options
    )
    driver.get("https://practicetestautomation.com/")
    driver.maximize_window()
    yield driver
    print("this is after each test case")
    driver.quit()