import configparser


configParser = configparser.RawConfigParser()   
configFilePath = r'C:\Users\PoojaP10\eclipse-workspace\nopcommerce\Configurations\config.ini'
configParser.read(configFilePath)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = configParser.get('common info','baseURL')
        return url
        
    @staticmethod
    def getUseremail():
        username = configParser.get('common info','useremail')
        return username
        
    @staticmethod
    def getPassword():
        password = configParser.get('common info','password')
        return password
        
    











