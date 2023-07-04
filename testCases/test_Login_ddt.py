import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from Screenshot import Screenshot
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup

class Test_002_Login:
    
    baseURL = ReadConfig.getApplicationURL()
    path = "C://Users//PoojaP10//eclipse-workspace//nopcommerce//TestData//testing.xlsx"
    
    
    logger = LogGen.loggen()
    
    def test_Login_ddt(self,setup):
        self.driver = setup
        
        self.logger.info("*********** TEST 002 DATA DRIVEN TESTING************")
        self.logger.info("************** VERIFY LOGIN TEST ************")

        #self.driver=webdriver.Chrome(executable_path="C:\Softwares\\chromedriver.exe")
        self.driver.get(self.baseURL)
        
        self.lp=LoginPage(self.driver)
        time.sleep(1)
        
        ### READING AND COUNTING OF EXCEL FILE
        
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows i a Excel:",self.rows)
        
        list_status=[]
        
        for r in range(2,self.rows + 1):
            self.user=XLUtils.readData(self.path, 'Sheet1', r, 1)
        
            self.password=XLUtils.readData(self.path, 'Sheet1', r, 2)
            
            self.exp=XLUtils.readData(self.path, 'Sheet1', r, 3)
            time.sleep(2)
            
            self.lp.setUserName(self.user)
            time.sleep(2)
            self.lp.setPassword(self.password)
            time.sleep(2)
            self.lp.clickLogin()
            
            time.sleep(2)
            
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            
            if act_title == exp_title:
                if self.exp=="Pass":
                    self.logger.info("****PASSED*******")
                    self.lp.clickLogout();
                    list_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("****FAILED*******")
                    self.lp.clickLogout();
                    list_status.append("Fail")
                    
            elif act_title != exp_title:
                if self.exp=="Pass":
                    self.logger.info("****failed*******")
                    list_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("****passsed******")
                    list_status.append("Pass")
                    
               
        if "Fail" not in list_status:
            self.logger.info("**LOGIN DATA DRIVEN TEST PASSED**")
            self.driver.close()
            assert True
        else:
            self.logger.info("** LOGIN DATA DRIVEN TEST FAILED**")
            self.driver.close()
            assert False
                
        self.logger.info("***  completed data driven test 002*****")
        
    
        
        
    































