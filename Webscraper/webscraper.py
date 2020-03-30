from bs4 import BeautifulSoup
from flask import Flask, render_template
import requests
source = requests.get('https://www.apartamentos-siesta.com/').text

soup = BeautifulSoup(source, 'lxml')
hotel_name = soup.find('h1').text

print(hotel_name)


source1 = requests.get('http://www.hotel-rural-can-beia.alaro.mallorca-vive.com/').text

soup1 = BeautifulSoup(source1, 'lxml')
hotel_nombre = soup.find('h1').select_one('span').text
print(hotel_nombre)
