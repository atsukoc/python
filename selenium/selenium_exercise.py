“””” 
This is a simple test script I wrote for a job interview at a local company
It shows test cases for successful and failed login
“”” 

import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class testLogin(unittest.TestCase):
    
    url = ''
    username = 'atsukoc'

    def setUp(self):
    
        self.driver = webdriver.Chrome('/Users/bailey/drivers/chromedriver')
        #self.driver = webdriver.Chrome('/Users/Atsuko/drivers/chromedriver')
    
    def getUsernameTextfield(self):
    
        return self.driver.find_element_by_id('username')
    
    def getPasswordTextfield(self):
    
        return self.driver.find_element_by_id('password')

    def getSignInButton(self):
    
        return self.driver.find_element_by_id('ext--login-submit')


    def test_login_fail(self):
        
        self.driver.get(self.url)
        
        # This is the error message that is supposed to be thrown when the authentication fails
        errorMessage = 'Incorrect username or password, please try again'

        # Get the html elements necessary for login (username & password textfields, login button)
        elem_username = self.getUsernameTextfield()
        elem_password = self.getPasswordTextfield()
        elem_loginButton = self.getSignInButton()

        # enter the username and password
        elem_username.clear()
        elem_password.clear()
        elem_username.send_keys(self.username)
        elem_password.send_keys('12345')  # this is an invalid password

        # click login button
        elem_loginButton.click()

        # Giving 10 seconds for the authentication to complete
        error = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'form--error')))
    
        # assert that the valid error message is thrown
        assert errorMessage in error.text
    
    

    def test_login_success(self):
        
        expectedTitle = 'Timeline - AtsukoC'
        
        self.driver.get(self.url)
        
        # Get the html elements necessary for login (username & password textfields, login button)
        elem_username = self.getUsernameTextfield()
        elem_password = self.getPasswordTextfield()
        elem_loginButton = self.getSignInButton()
        
        # enter the username and password
        elem_username.clear()
        elem_password.clear()
        elem_username.send_keys(self.username)
        elem_password.send_keys('abcde123')
        
        # click login button
        elem_loginButton.click()
        
        # Giving 10 seconds for the authentication to complete
        authentication = WebDriverWait(self.driver, 10).until(EC.title_is(expectedTitle))
        assert authentication == True
        
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

