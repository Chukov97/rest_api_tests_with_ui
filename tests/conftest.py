import pytest
from selene import browser
from selenium import webdriver
from settings import config


@pytest.fixture
def browser_management():
    browser.config.base_url = config.base_url
    browser.config.timeout = config.timeout
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = config.load_strategy
    browser.config.window_height = config.window_height
    browser.config.window_width = config.window_width
    browser.config.driver_options = driver_options

    yield

    browser.quit()
