import pytest
from selenium import webdriver
import pytest_html

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print('Launching chrome browser')
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print('Launching firefox browser')
    else:
        driver = webdriver.Chrome()

    return driver



def pytest_addoption(parser): #will get values from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #will return browser value to setup method
    return request.config.getoption("--browser")

### generating pytest html report

#it is hook fro adding env info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ruchira'

#it is hook fro delete/modify env info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
