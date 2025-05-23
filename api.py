from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["Catalogue_de_produits"]
produits = db["produits"]

# Convertisseur ObjectId → str
def serialize(produit):
    produit["_id"] = str(produit["_id"])
    return produit

@app.route("/api/produits", methods=["GET"])
def get_produits():
    resultats = list(produits.find())
    return jsonify([serialize(p) for p in resultats])

@app.route("/api/produits", methods=["POST"])
def ajouter_produit():
    data = request.json
    produits.insert_one(data)
    return jsonify({"message": "Produit ajouté"}), 201

@app.route("/api/produits/<id>", methods=["DELETE"])
def supprimer_produit(id):
    produits.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Produit supprimé"}), 200

@app.route("/api/produits/<id>", methods=["PUT"])
def modifier_produit(id):
    data = request.json
    produits.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "Produit modifié"}), 200

if __name__ == "__main__":
    app.run(debug=True)