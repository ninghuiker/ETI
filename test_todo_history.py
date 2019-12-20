from django.test import TestCase
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Test Case Scenario 1
def test_navigation_todo_history_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #Navigate to team contributions page
    driver.get('http://localhost:8000/todo/history/')
    assert "http://localhost:8000/todo/history/" == driver.current_url

test_navigation_todo_history_page()

