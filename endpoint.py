from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/party", methods=["GET"])
def get_party_json():
    with open("party.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run()