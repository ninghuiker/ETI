import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

def test_Navigation_application_homepage():
    #Navigate to application home page
    driver.get('http://localhost:8000/todo/')
    assert "http://localhost:8000/todo/" == driver.current_url

def test_todo_field():
    #Get the input textbox
    input_field = driver.find_element_by_name('content')
    input_field.clear()
    #enter input keyword
    input_field.send_keys("Singing")
    add_button = driver.find_element_by_xpath("//input[@type='submit']")
    add_button.click()
    assert "http://localhost:8000/todo/" == driver.current_url

