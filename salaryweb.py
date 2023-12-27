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
wait = WebDriverWait(driver, 10)

name=[]
with open("gifts.csv", "r") as file:
    next(file)
    for line in file:
        row=line.rstrip().split(";") 
        fname = row[0]
        name.append(fname)

for line in name:
    random_salary = random.randint(900, 2300)
    random_bonus = random.randint(200, 600)
    random_overtime = random.randint(0, 500)
    taxes = random_salary * 0.22
    find1 = driver.find_element(By.ID, "mat-input-3")
    find1.send_keys("Company X")
    find2 = driver.find_element(By.ID, "mat-input-6")
    find2.clear()
    find2.send_keys("2024/01/01")
    find3 = driver.find_element(By.ID, "mat-input-9")
    find3.clear()
    find3.send_keys(" ")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "mat-input-9"), " "))
    find4 = driver.find_element(By.ID, "mat-input-10")
    find4.clear()
    find4.send_keys(" ")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "mat-input-10"), " "))
    find5 = driver.find_element(By.ID, "mat-input-12")
    find5.clear()
    find5.send_keys(line)
    find6 = driver.find_element(By.ID, "mat-input-18")
    find6.clear()
    find6.send_keys(random_salary)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "mat-input-18"), str(random_salary)))
    find7 = driver.find_element(By.ID, "mat-input-19")
    find7.clear()
    find7.send_keys("Bonus")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "mat-input-19"), "Bonus"))
    find8 = driver.find_element(By.ID, "mat-input-20")
    find8.clear()
    find8.send_keys(random_bonus)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "mat-input-20"), str(random_bonus)))
    find9 = driver.find_element(By.ID, "mat-input-22")
    find9.clear()
    find9.send_keys(random_overtime)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "mat-input-22"), str(random_overtime)))
    find10 = driver.find_element(By.ID, "mat-input-24")
    find10.clear()
    find10.send_keys(taxes)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "mat-input-24"), str(taxes)))
    time.sleep(3)
    find11 = driver.find_element(By.CLASS_NAME, "mat-focus-indicator.mat-raised-button.mat-button-base.mat-primary")
    find11.click()
    find12 = wait.until(EC.element_to_be_clickable((By.ID, "download")))
    find12.click()
    driver.refresh()


input()