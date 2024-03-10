import configparser

config = configparser.RawConfigParser()
config.read("C:\\Web Testing\\NorCom_Pytest\\Configuration\\config.ini")

#config.read("..\\Configuration\\config.ini")

class Readconfig:
    @staticmethod
    def getEmail():
        Email = config.get('login data', 'email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'password')
        return Password

