from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import datetime
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

# Configuration MongoDB locale (à adapter)
app.config["MONGO_URI"] = "mongodb://localhost:27017/devlog"
mongo = PyMongo(app)

def serialize_log(log):
    log["_id"] = str(log["_id"])
    return log

@app.route("/", methods=["GET"])
def index():
    logs = list(mongo.db.logs.find().sort("date", -1))
    return render_template("index.html", logs=logs)

@app.route("/add", methods=["POST"])
def add_log():
    content = request.form.get("content")
    technologies = request.form.get("technologies", "")
    mood = request.form.get("mood", "productive")
    tech_list = [t.strip() for t in technologies.split(",") if t.strip()]

    new_log = {
        "content": content,
        "technologies": tech_list,
        "mood": mood,
        "date": datetime.datetime.now().isoformat()
    }

    mongo.db.logs.insert_one(new_log)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)