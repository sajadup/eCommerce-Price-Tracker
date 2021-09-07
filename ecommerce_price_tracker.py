import requests
from bs4 import BeautifulSoup
import smtplib
import time

headers = {
"User-Agent": "Paste Your User-Agent here"
}

# send a request to fetch HTML of the page
response = requests.get('https://www.amazon.in/New-Apple-iPhone-Mini-64GB/dp/B0932PTZ5V?ref_=ast_sto_dp&th=1&psc=1', headers=headers)

# create the soup object
soup = BeautifulSoup(response.content, 'html.parser')
soup.encode('utf-8')

# function to check if the price has dropped below certain amount
def check_price():
  title = soup.find(id= "productTitle").get_text()
  price = soup.find(class_ = "a-size-medium a-color-price priceBlockBuyingPriceString").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()

  #converting the string amount to float
  converted_price = float(price[0:5])
  print(converted_price)
  if(converted_price < 67000):
    send_mail()

  print(title.strip())

# function that sends an email if the prices fell down
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('sender_mail_id@gmail.com', 'password')

  subject = 'Price Drop'
  body = "Amazon link https://www.amazon.in/New-Apple-iPhone-Mini-64GB/dp/B0932PTZ5V?ref_=ast_sto_dp&th=1&psc=1"

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    'sender_mail_id@gmail.com',
    'receiver_mail_id@gmail.com',
    msg
  )
  #print a message to check if the email has been sent
  print('email sended')
  server.quit()

#loop that allows the program to regularly check for prices
while(True):
  check_price()
  time.sleep(60 * 60)