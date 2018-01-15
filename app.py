#!/sbin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, make_response, render_template, jsonify
import hashlib
import pandas as pd
from random import randint

app = Flask(__name__)

def get_user_fingerprint():
    return hashlib.sha1(request.remote_addr.encode("utf-8")).hexdigest()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/message", methods=["GET"])
def get_message():
    df = pd.read_csv("./data/messages.csv")
    data = df.iloc[randint(0, df.shape[0] - 1)]
    return data.to_json()

@app.route("/save", methods=["POST"])
def save():
    data = request.get_json()

    message = data["message"]
    sentiment = data["sentiment"]
    user = get_user_fingerprint()

    with open("./data/responses.csv", "a") as file:
        file.write(",".join([user, message, sentiment]))
        file.write("\n")

    return jsonify({"message": "Sucesso!"})
