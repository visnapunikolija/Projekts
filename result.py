import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas
import PyPDF2
import pathlib


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

#print(cheap_gift)
#print(expebsive_gift)
pdffolder = pathlib.Path("payslips")
pdf_payslip = list(pdffolder.glob("*.pdf"))

for f in range(len(pdf_payslip)):

    pdf_file=PyPDF2.PdfReader(open(pdf_payslip[f],"rb"))
    page = pdf_file.pages[0]
    text=page.extract_text()
    if gifter_name in text:
        pstn1=text.find("Employer Signature")
        pstn2 = (text[pstn1-8:pstn1])
        print(pstn2)


