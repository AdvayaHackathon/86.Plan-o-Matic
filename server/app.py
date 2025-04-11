from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# MongoDB setup
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["tourism"]
trips_collection = db["trips"]

@app.route("/api/trips", methods=["POST"])
def create_trip():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400

    result = trips_collection.insert_one(data)
    return jsonify({"message": "Trip saved!", "id": str(result.inserted_id)}), 201

@app.route("/", methods=["GET"])
def home():
    return "Flask backend is up and running!", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
