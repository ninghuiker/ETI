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
def test_navigation_team_contribution_page_with_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/accounts/login/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/nav/div/ul/li[3]/a").click()
    time.sleep(3)
    assert "http://localhost:8000/teamContributions/" == driver.current_url
    driver.close()


# Test Case Scenario 2
def test__team_contribution_page_without_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/teamContributions/")
    time.sleep(3)
    assert "http://127.0.0.1:8000/teamContributions/" == driver.current_url
    driver.close()


