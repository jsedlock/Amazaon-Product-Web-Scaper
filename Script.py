# import libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime
import pandas as pd
import datetime
import csv

import smtplib

# creating a function to send an email to myslef when the price drops

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('sedlockjeff1@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Macbook Pro price has dropped!"
    body = "Jeff, This is the moment we have been waiting for. Now is your chance to pick up the laptop of your dreams. Don't mess it up! Link here: https://www.amazon.com/Late-Apple-MacBookPro-Silver-Renewed/dp/B09Q4GQRXZ/ref=sr_1_1?crid=24FZTZWXRGVSK&keywords=16+in+macbook+pro+m1+16+gb+ram&qid=1682528722&sprefix=16+in+macbook+pro+m1+16+gb+ram%2Caps%2C93&sr=8-1"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'sedlockjeff1@gmail.com',
        msg
    )

def price_scrape():
  '''
  This function takes all the above code for web scraping amazon so it can be used in a timer 
  '''

  # Connect to Website
  URL = 'https://www.amazon.com/Late-Apple-MacBookPro-Silver-Renewed/dp/B09Q4GQRXZ/ref=sr_1_1?crid=24FZTZWXRGVSK&keywords=16+in+macbook+pro+m1+16+gb+ram&qid=1682528722&sprefix=16+in+macbook+pro+m1+16+gb+ram%2Caps%2C93&sr=8-1'

  headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15", 
         "Accept-Encoding":"gzip, deflate",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
           "DNT":"1",
           "Connection":"close", 
           "Upgrade-Insecure-Requests":"1"}
  
  page = requests.get(URL, headers=headers)

  # pulling all contents from the page into an HTML format
  soup1 = BeautifulSoup(page.content, 'html.parser')

  # adjusting the HTML format with the prettify format
  soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

  # now we will locate the title and price text from the html code
  title = soup2.find(id = 'productTitle').get_text()
  price = soup2.find("span", attrs={'class':'a-offscreen'}).get_text()

  # cleaning the string format for the title and price
  price = price.strip().replace('$' , '')
  price = float(price.replace(',', ''))
  title = title.strip()

  if price < 1689:
    send_mail()

  today = datetime.date.today()
  
  header = ['Product', 'Price', 'Date']
  data = [title, price, today]

  with open('Amazon_Macbook_Prices.csv', 'a+', newline='', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

    # putting the price_scrape function on a timer

while(True):
    price_scrape()
    time.sleep(86400)