from django.test import TestCase
import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select
#driver.implicitly_wait(30)


def login(driver):
    driver.get('http://localhost:8000/accounts/login/')
    username = driver.find_element_by_xpath('//*[@id="id_username"]')
    username.clear()
    username.send_keys("admin")
    password = driver.find_element_by_xpath('//*[@id="id_password"]')
    password.clear()
    password.send_keys("admin")
    btn = driver.find_element_by_xpath('/html/body/div/main/form/button')
    btn.click()
    time.sleep(1)
    todo = driver.find_element_by_xpath('/html/body/nav/div/ul/li[1]/a')
    todo.click()

# Test Case Scenario 1
def test_navigation_todo_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    login(driver)
    time.sleep(1) 
    driver.get('http://localhost:8000/todo/')
    assert "http://localhost:8000/todo/" == driver.current_url

test_navigation_todo_page()

# Test Case Scenario 2
def test_todo_field_regular_values():
    driver = webdriver.Chrome()
    driver.maximize_window()
    login(driver)
    time.sleep(1) 
    num_of_item = len(driver.find_elements_by_xpath("/html/body/div/main/div/ul/li"))
    input_field = driver.find_element_by_name('content')
    input_field.clear()
    input_field.send_keys("Watch anime")
    add_button = driver.find_element_by_xpath("/html/body/div/main/div/form/input[3]")
    add_button.click()
    time.sleep(1)
    final_num_of_item = len(driver.find_elements_by_xpath("/html/body/div/main/div/ul/li"))
    assert final_num_of_item > num_of_item
    assert "http://localhost:8000/todo/" == driver.current_url

test_todo_field_regular_values()

# Test Case Scenario 3
def test_todo_values_delete():
    driver = webdriver.Chrome()
    driver.maximize_window()
    login(driver)
    time.sleep(1)
    num_of_item = len(driver.find_elements_by_xpath("/html/body/div/main/div/ul/li"))
    delete_button = driver.find_element_by_xpath("/html/body/div/main/div/ul/li[1]/form/input[2]")
    delete_button.click()
    time.sleep(1)
    final_num_of_item = len(driver.find_elements_by_xpath("/html/body/div/main/div/ul/li"))
    assert final_num_of_item < num_of_item
    assert "http://localhost:8000/todo/" == driver.current_url

test_todo_values_delete()


# Test Case Scenario 4
def test_todo_field_empty():
    driver = webdriver.Chrome()
    driver.maximize_window()
    login(driver)
    time.sleep(1) 
    input_field = driver.find_element_by_name('content')
    input_field.clear()
    input_field.send_keys("")
    add_button = driver.find_element_by_xpath("/html/body/div/main/div/form/input[3]")
    add_button.click()
    assert "http://localhost:8000/todo/" == driver.current_url

test_todo_field_empty()



