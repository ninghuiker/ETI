from django.test import TestCase
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
#driver.implicitly_wait(30)

# Test Case Scenario 1
def test_navigation_registration_page():
   driver = webdriver.Chrome()
   driver.maximize_window()
   driver.get('http://localhost:8000/accounts/login/')
   driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()
   assert "http://localhost:8000/accounts/signup/" == driver.current_url

test_navigation_registration_page()

# Test Case Scenario 2
def test_registration_username_maxlength():
    driver = webdriver.Chrome()  
    driver.maximize_window()   
    driver.get('http://localhost:8000/accounts/login/')  
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()  
    driver.find_element_by_name("username").send_keys("t" * 151)  
    driver.find_element_by_name("password1").send_keys("passwordtest123") 
    driver.find_element_by_name("password2").send_keys("passwordtest123") 
    driver.find_element_by_xpath("/html/body/div/main/form/button").click() 
    time.sleep(1)  
    assert 'Login' == driver.title
      
test_registration_username_maxlength()

# Test Case Scenario 3
def test_registration_empty():
   driver = webdriver.Chrome()
   driver.maximize_window()
   driver.get('http://localhost:8000/accounts/login/')
   driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()
   driver.find_element_by_name("username").send_keys("")
   driver.find_element_by_name("password1").send_keys("")
   driver.find_element_by_name("password2").send_keys("")
   driver.find_element_by_xpath("/html/body/div/main/form/button").click()
   time.sleep(1)
   assert 'Sign Up' == driver.title

test_registration_empty()

# Test Case Scenario 4
def test_registration_username_maxlength_invalid_symbol():
    driver = webdriver.Chrome()  
    driver.maximize_window()   
    driver.get('http://localhost:8000/accounts/login/')  
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()  
    driver.find_element_by_name("username").send_keys("Themotherofmilkywaycontainsprecious9pizzasareMercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus, NeptuneandPluto.\!@#$^&*&*(^.^)*%$#@?/”")  
    driver.find_element_by_name("password1").send_keys("passwordtest123") 
    driver.find_element_by_name("password2").send_keys("passwordtest123") 
    driver.find_element_by_xpath("/html/body/div/main/form/button").click() 
    time.sleep(1)  
    error = driver.find_element_by_class_name("errorlist").text
    assert  "Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters." == error 
    
      
test_registration_username_maxlength_invalid_symbol()

# Test Case Scenario 5
def test_registration_empty_username():
    driver = webdriver.Chrome()
    driver.maximize_window()   
    driver.get('http://localhost:8000/accounts/login/')  
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()  
    driver.find_element_by_name("username").send_keys("")  
    driver.find_element_by_name("password1").send_keys("passwordtest123") 
    driver.find_element_by_name("password2").send_keys("passwordtest123") 
    driver.find_element_by_xpath("/html/body/div/main/form/button").click() 
    time.sleep(1)  
    assert 'Sign Up' == driver.title
      
test_registration_empty_username()

# Test Case Scenario 6
def test_registration_username_unique():
    driver = webdriver.Chrome()  
    driver.maximize_window()   
    driver.get('http://localhost:8000/accounts/login/')  
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()  
    driver.find_element_by_name("username").send_keys("@/.+-_test")  
    driver.find_element_by_name("password1").send_keys("passwordtest123") 
    driver.find_element_by_name("password2").send_keys("passwordtest123") 
    driver.find_element_by_xpath("/html/body/div/main/form/button").click() 
    time.sleep(1)  
    error = driver.find_element_by_class_name("errorlist").text
    assert  "Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters." == error
    assert 'Sign Up' == driver.title
      
test_registration_username_unique()

# Test Case Scenario 7
def test_registration_pw_only_num():
    driver = webdriver.Chrome()  
    driver.maximize_window()   
    driver.get('http://localhost:8000/accounts/login/')  
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()  
    driver.find_element_by_name("username").send_keys("testing1234599")  
    driver.find_element_by_name("password1").send_keys("12345678") 
    driver.find_element_by_name("password2").send_keys("12345678") 
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    time.sleep(1)
    error = driver.find_element_by_class_name("errorlist").text
    assert  'This password is too common.\nThis password is entirely numeric.' == error
    assert 'Sign Up' == driver.title
      
test_registration_pw_only_num()

# # Test Case Scenario 8
def test_registration_username_only_num():
    driver = webdriver.Chrome()  
    driver.maximize_window()   
    driver.get('http://localhost:8000/accounts/login/')  
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()  
    driver.find_element_by_name("username").send_keys("123123123")  
    driver.find_element_by_name("password1").send_keys("passwordtest123") 
    driver.find_element_by_name("password2").send_keys("passwordtest123") 
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    time.sleep(1)
    assert 'Login' == driver.title
      
test_registration_username_only_num()

# Test Case Scenario 9
def test_registration_existing_user():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/accounts/login/')
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()
    driver.find_element_by_name("username").send_keys("testing12345789")
    driver.find_element_by_name("password1").send_keys("passwordtest123")
    driver.find_element_by_name("password2").send_keys("passwordtest123")
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    time.sleep(1)
    driver.get('http://localhost:8000/accounts/login/')
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()
    driver.find_element_by_name("username").send_keys("testing12345789")
    driver.find_element_by_name("password1").send_keys("passwordtest123")
    driver.find_element_by_name("password2").send_keys("passwordtest123")
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    
    error = driver.find_element_by_class_name("errorlist").text
    assert  "A user with that username already exists." == error   

test_registration_existing_user()

# Test Case Scenario 10
def test_registration_pw_different():
    driver = webdriver.Chrome()  
    driver.maximize_window()   
    driver.get('http://localhost:8000/accounts/login/')  
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()  
    driver.find_element_by_name("username").send_keys("tester1")  
    driver.find_element_by_name("password1").send_keys("passwordtest123") 
    driver.find_element_by_name("password2").send_keys("passwordtest") 
    driver.find_element_by_xpath("/html/body/div/main/form/button").click() 
    time.sleep(1)
    error = driver.find_element_by_class_name("errorlist").text
    assert  "The two password fields didn’t match." == error     
    assert 'Sign Up' == driver.title
      
test_registration_pw_different()

# Test Case Scenario 11
def test_registration_username_unique_valid():
    driver = webdriver.Chrome()  
    driver.maximize_window()   
    driver.get('http://localhost:8000/accounts/login/')  
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()  
    driver.find_element_by_name("username").send_keys("finer@.@8")  
    driver.find_element_by_name("password1").send_keys("passwordtest123") 
    driver.find_element_by_name("password2").send_keys("passwordtest123") 
    driver.find_element_by_xpath("/html/body/div/main/form/button").click() 
    time.sleep(1)  
    assert 'Login' == driver.title
      
test_registration_username_unique_valid()

# Test Case Scenario 12
def test_registration_empty_password():
    driver = webdriver.Chrome()  
    driver.maximize_window()   
    driver.get('http://localhost:8000/accounts/login/')  
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()  
    driver.find_element_by_name("username").send_keys("tester1")  
    driver.find_element_by_name("password1").send_keys("") 
    driver.find_element_by_name("password2").send_keys("") 
    driver.find_element_by_xpath("/html/body/div/main/form/button").click() 
    time.sleep(1)  
    assert 'Sign Up' == driver.title
      
test_registration_empty_password()

# Test Case Scenario 13
def test_registration_password_8_chara():
    driver = webdriver.Chrome()  
    driver.maximize_window()   
    driver.get('http://localhost:8000/accounts/login/')  
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()  
    driver.find_element_by_name("username").send_keys("tester2")  
    driver.find_element_by_name("password1").send_keys("test123") 
    driver.find_element_by_name("password2").send_keys("test123") 
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    time.sleep(1)
    error = driver.find_element_by_class_name("errorlist").text
    assert  "The password is too similar to the username.\nThis password is too short. It must contain at least 8 characters.\nThis password is too common." == error
    assert 'Sign Up' == driver.title
      
test_registration_password_8_chara()

# Test Case Scenario 14
def test_registration_pw_common():
    driver = webdriver.Chrome()  
    driver.maximize_window()   
    driver.get('http://localhost:8000/accounts/login/')  
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()  
    driver.find_element_by_name("username").send_keys("tester3")  
    driver.find_element_by_name("password1").send_keys("password") 
    driver.find_element_by_name("password2").send_keys("password") 
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    time.sleep(1)
    error = driver.find_element_by_class_name("errorlist").text
    assert  'This password is too common.' == error
    assert 'Sign Up' == driver.title
      
test_registration_pw_common()

# Test Case Scenario 15
def test_registration_empty_cfm_password():
    driver = webdriver.Chrome()  
    driver.maximize_window()   
    driver.get('http://localhost:8000/accounts/login/')  
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()  
    driver.find_element_by_name("username").send_keys("tester1")  
    driver.find_element_by_name("password1").send_keys("passwordtest123") 
    driver.find_element_by_name("password2").send_keys("") 
    driver.find_element_by_xpath("/html/body/div/main/form/button").click() 
    time.sleep(1)  
    assert 'Sign Up' == driver.title
      
test_registration_empty_cfm_password()

# Test Case Scenario 16
def test_registration_successful():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/accounts/login/')
    driver.find_element_by_xpath("/html/body/div/main/p[2]/a").click()
    driver.find_element_by_name("username").send_keys("testing12345789")
    driver.find_element_by_name("password1").send_keys("passwordtest123")
    driver.find_element_by_name("password2").send_keys("passwordtest123")
    driver.find_element_by_xpath("/html/body/div/main/form/button").click()
    time.sleep(1)
    assert 'Login' == driver.title

test_registration_successful()
