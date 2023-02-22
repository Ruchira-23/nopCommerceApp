#this is a utility file from where we read all the common data that is stored in the ini file.
#Check ini file to know more about ini file

import configparser #predefined package in python

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini') #specify from which file the config var has to access the data

class ReadConfig():
    @staticmethod #can acces this method without creating any object just by the class name
    def getApplicationURL():
        url = config.get('common info', 'baseURl')
        return url

    @staticmethod  # can access this method without creating any object just by the class name
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod  # can acces this method without creating any object just by the class name
    def getPassword():
        password = config.get('common info', 'password')
        return password
