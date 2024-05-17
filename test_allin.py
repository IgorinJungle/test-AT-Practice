import os
import time

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--disable-cache")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 15, poll_frequency=1)


# @allure.feature()
# def test_firstly():
#     #Preconditions
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     login = ('xpath', '//input[@name = "username"]')
#     passwd = ('xpath', '//input[@name = "password"]')
#     submit = ('xpath', '//button[@type = "submit"]')
#
#
#     #action
#     wait.until(EC.visibility_of_element_located(login))
#     with allure.step("fill login"):
#         login_fill = driver.find_element(*login)
#         login_fill.send_keys("Admin")
#
#     with allure.step("fill password"):
#         passwd_fill = driver.find_element(*passwd)
#         passwd_fill.send_keys("admin123")
#
#     with allure.step("click submit button"):
#         submit_click = driver.find_element(*submit)
#         submit_click.click()


@allure.feature()
def test_submit():
    driver.get("https://testautomationpractice.blogspot.com/")

    with allure.step("Fill username"):
        name = driver.find_element('xpath', '//input[@id = "name"]')
        name.send_keys("Igor")

    with allure.step("Fill EMAIL"):
        email = driver.find_element('xpath', '//input[@id = "email"]')
        email.send_keys("mymail@mail.com")

    with allure.step("Fill Phone"):
        phone = driver.find_element('xpath', '//input[@id = "phone"]')
        phone.send_keys("+7 800 555 35-35")

    with allure.step("Fill Adress"):
        adress = driver.find_element("xpath", '//textarea[@id = "textarea"]')
        adress.send_keys("Moscow, Bolschaya Nikitskaya 27,1")
        








