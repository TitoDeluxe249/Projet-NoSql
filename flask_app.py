from flask import Flask, jsonify, request
from bson import ObjectId
from db import collection

app = Flask(__name__)

def serialize(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@app.route("/api/produits", methods=["GET"])
def get_produits():
    return jsonify([serialize(p) for p in collection.find()])

@app.route("/api/produits", methods=["POST"])
def add_produit():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Produit ajouté"}), 201

if __name__ == "__main__":
    app.run(port=5000)