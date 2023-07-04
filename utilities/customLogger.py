import logging
import inspect

class LogGen():
    @staticmethod
    def loggen():
        #filepath = 'C://Users//PoojaP10//eclipse-workspace//nopcommerce//Logs//automation.log'
        #filepath = r'./Logs/automation.log'
        logging.basicConfig(filename='C://Users//PoojaP10//eclipse-workspace//nopcommerce//Logs//automation.log',
                           format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y%I:%M:%S %p',force=True)
    
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
    
    
    #def loggen(self,loglevel=logging.DEBUG):
        #logger_name = inspect.stack()[1][3]
        #logger = logging.getLogger(logger_name) 
        #logger.setLevel(loglevel)
        #fh = logging.FileHandler("./logs/automation.log", mode='a')
        
        #formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y%I:%M:%S %p')
        ##fh.setFormatter(formatter)
        #logger.addHandler(fh)
        #return logger


    
    