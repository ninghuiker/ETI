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



# Test Case Scenario 1
def test_navigation_login_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to the login page
    driver.get("http://localhost:8000/accounts/login/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    assert 'Home' == driver.title
    driver.close()


# Test Case Scenario 2
def test_navigation_registration_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to the registration page
    driver.get('http://127.0.0.1:8000/accounts/signup/')
    time.sleep(2)
    assert "http://127.0.0.1:8000/accounts/signup/" == driver.current_url
    driver.close()



# Test Case Scenario 3
def test_navigation_todo_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to the todo page
    driver.get('http://127.0.0.1:8000/todo/')
    time.sleep(2)
    assert "http://127.0.0.1:8000/todo/" == driver.current_url
    driver.close()



# Test Case Scenario 4
def test_navigation_todo_history_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to the todo history page
    driver.get('http://127.0.0.1:8000/todo/history/')
    time.sleep(2)
    assert "http://127.0.0.1:8000/todo/history/" == driver.current_url
    driver.close()


# Test Case Scenario 5
def test_navigation_team_contribution_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to the team contribution page
    driver.get('http://127.0.0.1:8000/teamContributions/')
    time.sleep(2)
    assert "http://127.0.0.1:8000/teamContributions/" == driver.current_url
    driver.close()



