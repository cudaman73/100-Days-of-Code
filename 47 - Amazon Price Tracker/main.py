import requests
from bs4 import BeautifulSoup
import smtplib
from config import EMAIL, G_APP_KEY
import lxml

AMAZON_URL = "https://www.amazon.com/dp/B07CT9BH2T/"

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept-Language': 'en-US,en;q=0.5'
}

response = requests.get(AMAZON_URL, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')

product_name = soup.find(name="span", id="productTitle").get_text(strip=True).encode('ascii', 'ignore').decode('ascii')
price = float(soup.find(name="span", class_='a-price-whole').text +
              soup.find(name="span", class_='a-price-fraction').text)

data = f"{product_name} is now only {price}! Purchase at: \n{AMAZON_URL}"

if price < 80:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=G_APP_KEY)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:Amazon Low Price Alert!\n\n{data}")
else:
    print(f"Price is {price}, not low enough to email about")
