import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas
import PyPDF2

print("Type in your name:")
gifter_name = input()

fails = pandas.read_excel("names.xlsx", sheet_name="names")
info_list = fails.values.tolist()
for line in range(len(info_list)):
    i=info_list[line][0]
    if i == gifter_name:
        giftreceiver_name = info_list[line][1]
        break

print(giftreceiver_name)

with open("gifts.csv", "r") as file:
    next(file)
    for line in file:
        if giftreceiver_name in line:
            row=line.rstrip().split(";") 
            cheap_gift = row[1]
            expebsive_gift = row[2]
            break
        row=line.rstrip().split(";") 

print(cheap_gift)
print(expebsive_gift)
