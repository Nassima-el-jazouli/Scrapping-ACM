import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['Scrapped_Data']
collection = db['Data']


with open('ieeePro.json') as file:
    file_data = json.load(file)

collection.insert_many(file_data)

client.close()