# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import driver

def logout(driver):
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to_alert().accept()

def test_login(driver):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("submit").click()

def test_login(driver):
    driver.get("http://localhost/php4dvd/")
    login(driver)
    logout(driver)