import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseURl = ReadConfig.getApplicationURL()  # implemented in readproperties file. as it is a static methid no need to create any object
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):  # setup is a onetime creation of driver, instead of writing webdriver.chrome everywhere just use set which is defined in the conftest file
        self.logger.info("********Test_001_Login*************")
        self.logger.info("********Verifying Home page Title***********")
        self.driver = setup
        self.driver.get(self.baseURl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********Home Page title test is passed************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********Home page title test is failed*************")
            assert False

    def test_login(self, setup):
        self.logger.info("********Verifying login test*************")

        self.driver = setup
        self.driver.get(self.baseURl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title


        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********login test is passed*************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********login test is failed*************")
            assert False
