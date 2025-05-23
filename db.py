from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Catalogue_de_produits"]
collection = db["produits"]