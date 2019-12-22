from django.test import TestCase
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
#driver.implicitly_wait(30)

# Test Case Scenario 1
def test_navigation_todo_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to the todo page
    driver.get('http://localhost:8000/todo/')
    assert "http://localhost:8000/todo/" == driver.current_url

test_navigation_todo_page()

# Test Case Scenario 3
def test_todo_field_empty():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to application home page
    driver.get('http://localhost:8000/todo/')
    assert "http://localhost:8000/todo/" == driver.current_url
    #Get the input textbox
    input_field = driver.find_element_by_name('content')
    input_field.clear()
    #enter input keyword
    input_field.send_keys("")
    add_button = driver.find_element_by_xpath("/html/body/form/input[3]")
    add_button.click()
    assert "http://localhost:8000/todo/" == driver.current_url

test_todo_field_empty()

# Test Case Scenario 3
def test_todo_field_regular_values():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to application home page
    driver.get('http://localhost:8000/todo/')
    assert "http://localhost:8000/todo/" == driver.current_url
    #Get the input textbox
    input_field = driver.find_element_by_name('content')
    input_field.clear()
    #enter input keyword
    input_field.send_keys("Play Final Fantasy XIII")
    add_button = driver.find_element_by_xpath("/html/body/form/input[3]")
    add_button.click()
    assert "http://localhost:8000/todo/" == driver.current_url

test_todo_field_regular_values()

# Test Case Scenario 4
def test_todo_field_unique_values():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to application home page
    driver.get('http://localhost:8000/todo/')
    assert "http://localhost:8000/todo/" == driver.current_url
    #Get the input textbox
    input_field = driver.find_element_by_name('content')
    input_field.clear()
    #enter input keyword
    input_field.send_keys('~`!@#$%^&*()_+}{":<>?|/')
    add_button = driver.find_element_by_xpath("/html/body/form/input[3]")
    add_button.click()
    assert "http://localhost:8000/todo/" == driver.current_url

test_todo_field_unique_values()

# Test Case Scenario 5
def test_todo_field_regular_and_unique_values():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to application home page
    driver.get('http://localhost:8000/todo/')
    assert "http://localhost:8000/todo/" == driver.current_url
    #Get the input textbox
    input_field = driver.find_element_by_name('content')
    input_field.clear()
    #enter input keyword
    input_field.send_keys("Hang out with friends! 8^.^8")
    add_button = driver.find_element_by_xpath("/html/body/form/input[3]")
    add_button.click()
    assert "http://localhost:8000/todo/" == driver.current_url

test_todo_field_regular_and_unique_values()

# Test Case Scenario 6
def test_todo_values_delete():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to application home page
    driver.get('http://localhost:8000/todo/')
    assert "http://localhost:8000/todo/" == driver.current_url
    #Get the input textbox
    input_field = driver.find_element_by_name('content')
    input_field.clear()
    #enter input keyword
    input_field.send_keys("Testing")
    add_button = driver.find_element_by_xpath("/html/body/form/input[3]")
    add_button.click()
    assert "http://localhost:8000/todo/" == driver.current_url
    #delete added text
    delete_button = driver.find_element_by_xpath("/html/body/ul/li[1]/form/input[2]")
    delete_button.click()
    assert "http://localhost:8000/todo/" == driver.current_url

test_todo_values_delete()