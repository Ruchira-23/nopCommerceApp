import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLutils

class Test_002_DDT_Login:
    baseURl = ReadConfig.getApplicationURL()  # implemented in readproperties file. as it is a static methid no need to create any object
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("********Test_002_DDt_Login********")
        self.logger.info("********Verifying login test*************")

        self.driver = setup
        self.driver.get(self.baseURl)

        self.lp = LoginPage(self.driver)

        self.rows=XLutils.getRowCount(self.path, 'Sheet1')
        print('Number of rows in excel:',self.rows)

        lst_status=[] #empty list var

        for r in range(2,self.rows+1):
            self.user = XLutils.readData(self.path, 'Sheet1',r,1)
            self.password = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLutils.readData(self.path, 'Sheet1', r, 3)


            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("Test is passed")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("Fail")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("Fail")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("Pass")
                    lst_status.append("Pass")


        if "Fail" not in lst_status:
            self.logger.info("Login DDt Test is passed")
            self.driver.close()
            assert True

        else:
            self.logger.info("Login DDT failed")
            self.driver.close()
            assert False


        self.logger.info("End of DDt testing")






