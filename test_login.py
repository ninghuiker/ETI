from django.test import TestCase
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Test Case Scenario 1
def test_navigation_login_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/accounts/login/")
    assert 'Login' == driver.title
    
    driver.close()
    
test_navigation_login_page()

# Test Case Scenario 2
def test_admin_login_empty():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/accounts/login/")
    driver.find_element_by_name("username").send_keys("")
    driver.find_element_by_name("password").send_keys("passwordtest123")
    driver.find_element_by_xpath("/html/body/main/form/button").click()
    assert 'Login' == driver.title
    
    driver.close()

test_admin_login_empty()

# Test Case Scenario 3
def test_admin_login_empty_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/accounts/login/")
    driver.find_element_by_name("username").send_keys("")
    driver.find_element_by_name("password").send_keys("passwordtest123")
    driver.find_element_by_xpath("/html/body/main/form/button").click()
    assert 'Login' == driver.title
    
    driver.close()

test_admin_login_empty_password()

# Test Case Scenario 4
def test_admin_login_empty_username():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/accounts/login/")
    driver.find_element_by_name("username").send_keys("")
    driver.find_element_by_name("password").send_keys("passwordtest123")
    driver.find_element_by_xpath("/html/body/main/form/button").click()
    assert 'Login' == driver.title
    
    driver.close()

test_admin_login_empty_username()

# Test Case Scenario 5
def test_admin_login_wrong_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/accounts/login/")
    driver.find_element_by_name("username").send_keys("peter")
    driver.find_element_by_name("password").send_keys("%&$*#")
    driver.find_element_by_xpath("/html/body/main/form/button").click()
    error = driver.find_element_by_class_name("errorlist").text
    assert 'Login' == driver.title
    assert 'Please enter a correct username and password. Note that both fields may be case-sensitive.' == error
    
    driver.close()

test_admin_login_wrong_password()

# Test Case Scenario 6
def test_admin_login_wrong_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/accounts/login/")
    driver.find_element_by_name("username").send_keys("%^&*()%$#@#& *&*&$_+++++&&&&?????/ #*")
    driver.find_element_by_name("password").send_keys("%%%%%")
    driver.find_element_by_xpath("/html/body/main/form/button").click()
    error = driver.find_element_by_class_name("errorlist").text
    assert 'Login' == driver.title
    assert 'Please enter a correct username and password. Note that both fields may be case-sensitive.' == error
    
    driver.close()

test_admin_login_wrong_credentials()

# Test Scenario 7
def test_admin_valid_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/accounts/login/")
    driver.find_element_by_name("username").send_keys("peter")
    driver.find_element_by_name("password").send_keys("passwordtest123")
    driver.find_element_by_xpath("/html/body/main/form/button").click()
    assert 'Home' == driver.title
    
    driver.close()

test_admin_valid_login()



