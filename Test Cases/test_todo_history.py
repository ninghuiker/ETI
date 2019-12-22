from django.test import TestCase
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Test Case Scenario 1
def test_navigation_todo_history_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Login 
    driver.get("http://localhost:8000/accounts/login/")
    driver.find_element_by_name("username").send_keys("finer")
    driver.find_element_by_name("password").send_keys("passwordtest123")
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    #Navigate to todo history page
    driver.find_element_by_xpath("/html/body/nav/div/ul/li[2]/a").click()
    assert "http://localhost:8000/todo/history/" == driver.current_url

test_navigation_todo_history_page()

