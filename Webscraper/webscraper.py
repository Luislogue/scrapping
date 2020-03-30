from bs4 import BeautifulSoup
from flask import Flask, render_template
import requests
source = requests.get('https://www.apartamentos-siesta.com/').text

soup = BeautifulSoup(source, 'lxml')
hotel_name = soup.find('h1').text
for hotel_price in soup.find_all('div',class_="price-tag-home"):
     if len(hotel_price["class"]) != 1:
         continue;
print(hotel_name)
print(hotel_price)