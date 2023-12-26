import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://paysliper.com/payslip-generator"
driver.get(url)
time.sleep(2)

random_salary = random.randint(1000, 2500)
random_overtime = random.randint(0, 500)

print(random_salary)

find1 = driver.find_element(By.ID, "mat-input-3")
find1.send_keys("Company X")
find2 = driver.find_element(By.ID, "mat-input-6")
find2.clear()
find2.send_keys("2024/01/01")
#find = driver.find_element(By.ID, "mat-input-8")
#find.send_keys("2023/12/01 - 2023/12/31")
find3 = driver.find_element(By.ID, "cdk-drop-list-2")
find3_1 = find3.find_element(By.CLASS_NAME, "cdk-drag paysliper-slip-content")
find3_2 = find3_1.find_element(By.CLASS_NAME, "mat-focus-indicator mat-icon-button mat-button-base")
find3_2.click()
find = driver.find_element(By.ID, "mat-input-18")
find.clear()
find.send_keys(random_salary)
find = driver.find_element(By.ID, "mat-input-22")
find.clear()
find.send_keys(random_overtime)


input()