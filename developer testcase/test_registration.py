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
def test_navigation_registration_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to the todo page
    driver.get('http://127.0.0.1:8000/accounts/signup/')
    assert "http://127.0.0.1:8000/accounts/signup/" == driver.current_url
    driver.close()


# Test Case Scenario 2
def test_create_user_successful():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/accounts/signup/")
    driver.find_element_by_name("username").send_keys("Asaudias845")
    driver.find_element_by_name("password1").send_keys("123465asdxxyuoih")
    driver.find_element_by_name("password2").send_keys("123465asdxxyuoih")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()  
    assert 'Login' == driver.title
    time.sleep(2)
    driver.close()


# Test Case Scenario 3
def test_create_user_empty_fields():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/accounts/signup/")
    driver.find_element_by_name("username").send_keys("")
    driver.find_element_by_name("password1").send_keys("")
    driver.find_element_by_name("password2").send_keys("")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    #ermsg1 = driver.find_element_by_name("'username'.getAttribute('validationMessage')").text
    #assert 'Please fill out this field.' == ermsg1 and 'http://127.0.0.1:8000/accounts/signup/' == driver.title
    assert 'Sign Up' == driver.title
    time.sleep(2)
    driver.close()


# Test Case Scenario 4
def test_create_user_empty_username_fields():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/accounts/signup/")
    driver.find_element_by_name("username").send_keys("")
    driver.find_element_by_name("password1").send_keys("12345612")
    driver.find_element_by_name("password2").send_keys("12345612")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    #ermsg1 = driver.find_element_by_name("'username'.getAttribute('validationMessage')").text
    #assert 'Please fill out this field.' == ermsg1 and 'http://127.0.0.1:8000/accounts/signup/' == driver.title
    assert 'Sign Up' == driver.title
    time.sleep(2)
    driver.close()


# Test Case Scenario 5
def test_create_user_empty_password_fields():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/accounts/signup/")
    driver.find_element_by_name("username").send_keys("testing456")
    driver.find_element_by_name("password1").send_keys("")
    driver.find_element_by_name("password2").send_keys("")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()  
    assert 'Sign Up' == driver.title
    time.sleep(2)
    driver.close()


# Test Case Scenario 6
def test_create_user_confirm_password_fields_empty():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/accounts/signup/")
    driver.find_element_by_name("username").send_keys("testing456")
    driver.find_element_by_name("password1").send_keys("abcd123456789")
    driver.find_element_by_name("password2").send_keys("")
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    assert 'Sign Up' == driver.title
    time.sleep(2)
    driver.close()



# Test Case Scenario 7
def test_create_user_confirm_password_fields_unmatch():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/accounts/signup/")
    driver.find_element_by_name("username").send_keys("testing456")
    driver.find_element_by_name("password1").send_keys("abcd123456789")
    driver.find_element_by_name("password2").send_keys("abckjdbsadbbiuub")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    #ermsg1 = driver.find_element_by_xpath("//*[contains(text(), 'The two password fields didnt match.')]").text
    #assert 'The two password fields didnt match' == ermsg1 and 'Sign Up' == driver.title
    assert 'Sign Up' == driver.title
    time.sleep(2)
    driver.close()


# Test Case Scenario 8
def test_create_user_password_lessthan_8_character():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/accounts/signup/")
    driver.find_element_by_name("username").send_keys("testing456")
    driver.find_element_by_name("password1").send_keys("abcd12")
    driver.find_element_by_name("password2").send_keys("abcd12")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    assert 'Sign Up' == driver.title
    time.sleep(2)
    driver.close()
    
# Test Case Scenario 9
def test_create_user_password_too_common():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/accounts/signup/")
    driver.find_element_by_name("username").send_keys("testing456")
    driver.find_element_by_name("password1").send_keys("abcd12")
    driver.find_element_by_name("password2").send_keys("abcd12")
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    time.sleep(2)
    assert 'Sign Up' == driver.title
    time.sleep(2)
    driver.close()


# Test Case Scenario 10
def test_create_user_password_entire_numeric():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/accounts/signup/")
    driver.find_element_by_name("username").send_keys("testing456")
    driver.find_element_by_name("password1").send_keys("1234567890")
    driver.find_element_by_name("password2").send_keys("1234567890")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    assert 'Sign Up' == driver.title
    time.sleep(2)
    driver.close()

