from selenium import webdriver
import pytest
#import hooks
#from _pytest.config import PytestPluginManager
#global PytestPluginManager

"""def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pooja'
    
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home",None)
    metadata.pop("Plugins",None)"""


@pytest.fixture()

def setup():   
    driver = webdriver.Chrome(executable_path="C:\Softwares\\chromedriver.exe")
    return driver



"""def pytest_adaption(parser,PytestPluginManager):
    parser.addoption("--browser")
    
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



## to generate report"""











