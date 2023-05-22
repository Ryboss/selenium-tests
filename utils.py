import time

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime
from typing import Optional


class Page(object):
    driver = None

    def __init__(self, web_driver, url: str = ''):
        self.driver = web_driver
        self.get(url)

    def get(self, url: str):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def login_in_bank(self, driver):
        """
        Автоирзация за Harry Potter
        """

        # Нажатие на кнопку Customer Login
        element5 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-primary.btn-lg")))
        element5.click()

        # Выбор Harry Potter
        select = Select(WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "form-control.ng-pristine.ng-untouched.ng-valid"))))
        select.select_by_visible_text("Harry Potter")

        # Нажатие на кнопку login
        element_login = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-default")))
        element_login.click()
        time.sleep(2)

    @staticmethod
    def get_fib_number(number: int = int(datetime.now().strftime("%d"))):
        """
        Получение числа фибоначи
        """

        first_number = 1
        second_number = 1
        fib_list = [0, 1]

        for i in range(number):
            fib_list.append(second_number)
            third_number = first_number
            first_number = second_number
            second_number = third_number + second_number

        return fib_list[number - 1]
