import time
import csv

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from typing import List

from utils import Page
webdriver.Chrome().find_elements()

def test_login_in_bank():
    """
    Автоирзация за Harry Potter
    """

    driver = webdriver.Chrome()
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    # Нажатие на кнопку Customer Login
    element5 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-primary.btn-lg")))
    print(driver.current_url)
    element5.click()
    print(driver.current_url)

    # Выбор Harry Potter
    select = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "form-control.ng-pristine.ng-untouched.ng-valid"))))
    select.select_by_visible_text("Harry Potter")

    # Нажатие на кнопку login
    element_login = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-default")))
    element_login.click()
    time.sleep(2)
    print(driver.current_url)

    deposit_number = get_fib_number()
    deposit_page = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "borderM.box.padT20.ng-scope")))
    deposit = deposit_page.find_elements(By.CLASS_NAME, "center")
    deposit_button = deposit[len(deposit) - 1]
    deposit_button.click()

    amount = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "form-control.ng-pristine.ng-untouched.ng-invalid.ng-invalid-required")))
    time.sleep(2)
    amount.send_keys(deposit_number)
    button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-default")))
    button.click()
    time.sleep(2)

    withdrawl = driver.find_elements(By.CLASS_NAME, "btn.btn-lg.tab")
    time.sleep(2)
    print(withdrawl)
    withdrawl_button = withdrawl[len(withdrawl) - 1]
    print(withdrawl_button)
    withdrawl_button.click()
    withdrawl_amount = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "form-control.ng-pristine.ng-untouched.ng-invalid.ng-invalid-required")))
    time.sleep(2)
    print(withdrawl_amount)
    withdrawl_amount = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "form-control.ng-pristine.ng-untouched.ng-invalid.ng-invalid-required")))
    withdrawl_amount.send_keys(deposit_number)
    time.sleep(2)
    withdrawl_button_submit = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-default")))
    withdrawl_button_submit.click()
    time.sleep(2)
    balance = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "center")))
    balance_number = balance.find_elements(By.CLASS_NAME, "ng-binding")
    print(balance_number[1].text)
    assert int(balance_number[1].text) == 0
    print(balance_number[1].text)
    transaktions_page = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-lg.tab")))
    print(transaktions_page.text)
    transaktions_page.click()
    transaktions = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "table.table-bordered.table-striped")))
    transaktions_list = transaktions.find_elements(By.CLASS_NAME, "ng-scope")
    print(transaktions_list)
    assert len(transaktions_list) == 2
    transaction_list_end = []
    for trans in transaktions_list:
        transaction_list_end.append(trans.text)
        print(trans.text)
    time.sleep(2)
    generate_csv_report(transaction_list_end)


def generate_csv_report(rows: List[str]):
    """
    Генерация csv отчета
    """

    with open("report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Sum", "Transactions type"])
        for row in rows:
            row_list = row.split(" ")
            time = f"{row_list[1].replace(',', '')} {row_list[0]} {row_list[2]} {row_list[3]}"
            writer.writerow([time, row_list[5], row_list[6]])

        file.close()


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

login_in_bank()
