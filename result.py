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


print("Lūdzu, ievadiet savu vārdu:")
gifter_name = input()

fails = pandas.read_excel("names.xlsx", sheet_name="names")
info_list = fails.values.tolist()
for line in range(len(info_list)):
    i=info_list[line][0]
    if i == gifter_name:
        giftreceiver_name = info_list[line][1]
        break

print("Kolēģis, kuram jūs dāvināt davanu ir:")
print(giftreceiver_name)

with open("gifts.csv", "r") as file:
    next(file)
    for line in file:
        if giftreceiver_name in line:
            row=line.rstrip().split(";") 
            cheap_gift = row[1]
            expensive_gift = row[2]
            break
        



pdffolder = pathlib.Path("payslips")
pdf_payslip = list(pdffolder.glob("*.pdf"))

for f in range(len(pdf_payslip)):

    pdf_file=PyPDF2.PdfReader(open(pdf_payslip[f],"rb"))
    page = pdf_file.pages[0]
    text=page.extract_text()
    if gifter_name in text:
        pstn1=text.find("Employer Signature")
        pstn2 = (text[pstn1-8:pstn1])
        pstn3=float(pstn2.rstrip())
        break


if int(pstn3) < 1600:
    true_gift = cheap_gift
else:
    true_gift = expensive_gift




service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
url = "https://220.lv/ru?gad_source=1&gclid=EAIaIQobChMIwti9icivgwMVgaeDBx26sAjNEAAYASAAEgInqvD_BwE"
driver.get(url)
time.sleep(2)

find1 = driver.find_element(By.CLASS_NAME, "c-btn--secondary.h-btn--small.cookies_accept-all")
find1.click()
time.sleep(2)
find2 = driver.find_element(By.ID, "searchInput")
find2.send_keys(true_gift)
find3 = driver.find_element(By.CLASS_NAME, "c-search__submit")
find3.click()
find4 = driver.find_element(By.CLASS_NAME, "product-item-inner.height-countdown.heightResponse")
find4.click()
find5 = driver.find_element(By.CLASS_NAME, "c-btn--primary.h-btn-intent--atc")
find5.click()
time.sleep(2)
find6 = driver.find_element(By.ID, "buy")
find6.click()
input()