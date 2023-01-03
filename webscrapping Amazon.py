# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# Connect to Website and pull in data

URL = 'https://www.amazon.com/Logitech-Headset-H390-Noise-Cancelling/dp/B000UXZQ42/ref=pd_day0fbt_img_sccl_2/134-5424659-2770240?pd_rd_w=FN4IK&content-id=amzn1.sym.c2062204-a945-491b-941c-359f18d6fec5&pf_rd_p=c2062204-a945-491b-941c-359f18d6fec5&pf_rd_r=F7NHPAB0TXPW31HR94F9&pd_rd_wg=tbFYr&pd_rd_r=c1923a74-5aca-490b-bc92-26ea67b12fdd&pd_rd_i=B000UXZQ42&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1" }
page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content,'html.parser')

soup2 = BeautifulSoup(soup1.prettify(),'html.parser')
title = soup2.find(id='productTitle').getText()
price = soup2.find(id = 'corePrice_feature_div').getText()



title = title.strip()
price = price.strip()[1:7]

import datetime
today = datetime.date.today()

import csv

header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open('AmazonWebScrapper.csv', 'w', newline='', encoding = 'UTF8') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  writer.writerow(data)




# Now we are appended data
with open('AmazonWebScrapper.csv', 'a+', newline='', encoding = 'UTF8') as f:
  writer = csv.writer(f)
  writer.writerow(data)

import pandas as pd

file_read = pd.read_csv(r"C:\Users\canar\OneDrive\Documents\Python Practice\AmazonWebScrapper.csv")
print(file_read)
