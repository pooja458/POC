from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class LoginPage:
    textbox_username_xpath ="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input"
    textbox_password_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input"
    textbox_login_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_xpath="/html/body/div[3]/nav/div/ul/li[3]/a"
    
    
    def __init__(self,driver):
        self.driver = driver
        
    
    def setUserName(self,username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        #action = ActionChains(self,driver)
        #action.key_down(Keys.CONTROL).send_keys('A').send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()   

        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)
        
    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
        
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.textbox_login_xpath).click()
        
    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

        
        
































