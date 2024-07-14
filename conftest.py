import pytest
from selenium import webdriver
from stuff.pathways import Pathways

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
