from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Catalogue_de_produits"]

produit = {"nom": "iPhone 14", "prix": 1099, "stock": 10}
db.produits.insert_one(produit)

print("Produit ajouté.")