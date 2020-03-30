
from flask import Flask, redirect, render_template, request
from bs4 import BeautifulSoup
from flask import Flask, render_template
import requests
from flask_pymongo import pymongo

app=Flask(__name__)
# client = pymongo.MongoClient("mongodb+srv://lulogue97@gmail.com:battlefield3@cluesterprueba-f7dzy.mongodb.net/test?retryWrites=true&w=majority")
# db = client.scrapping
# collection = db['hoteles']


@app.route('/')
def index():
    source = requests.get('https://www.apartamentos-siesta.com/').text
    soup = BeautifulSoup(source, 'lxml')
    hotel_name = soup.find('h1').text
    for hotel_price in soup.find_all('div',class_="price-tag-home"):
     if len(hotel_price["class"]) != 1:
         continue;
    # db.collection.insert(hotel_name, hotel_price)
    return render_template('index.html', hotel_name=hotel_name, hotel_price=hotel_price)
    

if __name__ == "__main__":
    app.run('0.0.0.0',5000,debug=True)