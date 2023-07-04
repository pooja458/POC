import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from Screenshot import Screenshot
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup

class Test_001_Login:
    
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    
    logger = LogGen.loggen()
    
    def test_homePageTitle(self,setup):
        self.logger.info("******* TEST_001*********")
        self.logger.info("*****VERIFY TITLE*****")
        self.driver = setup
        #self.driver=webdriver.Chrome(executable_path="C:\Softwares\\chromedriver.exe")
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*****VERIFY TITLE PASS*****")

        else:
            self.driver.save_screenshot("C://Users//PoojaP10//eclipse-workspace//nopcommerce//Screenshots//test_homePageTitle.png")
            Screenshot = Image.open("test_homePageTitle.png")
            Screenshot.show()
            #self.driver.get_screenshot_as_file(".\\Screenshots\\test_homePageTitle.png") 
            self.logger.error("************** VERIFY TITLE FAILED ************")
        
            self.driver.close()
            assert False
            
            
    def test_Login(self,setup):
        self.driver = setup
        self.logger.info("************** VERIFY LOGIN TEST ************")

        #self.driver=webdriver.Chrome(executable_path="C:\Softwares\\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        time.sleep(1)
        self.lp.setUserName(self.username)
        time.sleep(1)
        self.lp.setPassword(self.password)
        time.sleep(1)
        self.lp.clickLogin()
        time.sleep(1)
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************** LOGIN TEST PASSED ************")
            self.driver.close()
        else:
            self.driver.save_screenshot("C://Users//PoojaP10//eclipse-workspace//nopcommerce//Screenshots//test_login.png")
            Screenshot = Image.open("test_login.png")
            Screenshot.show()
            self.logger.error("************** LOGIN TEST FAILED ************")

            self.driver.close()
            assert False
            
            

        
        
        
    
        
        
    































