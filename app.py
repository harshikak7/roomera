"""Roomera backend + frontend server.
Run:  pip install -r requirements.txt  &&  python app.py
Open: http://localhost:5000
"""
import os
from flask import Flask, request, jsonify, send_from_directory
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

# Fake dataset: answers to 6 would-you-rather questions (0 = option A, 1 = option B)
ANSWERS = [[1,0,1,0,0,1],[0,0,1,1,0,1],[0,0,0,0,0,0],[0,0,0,0,0,1],
           [1,1,1,1,0,0],[0,0,0,0,0,1],[1,1,0,1,1,0],[0,1,1,1,0,0]]
USERS = [{"id": i + 1, "ans": a} for i, a in enumerate(ANSWERS)]
WEIGHTS = np.array([1.5, 1.5, 1, 1, 0.5, 1])  # sleep & cleanliness matter most


def compatibility(mine, theirs):
    """Weighted agreement score, 0-100."""
    agree = (np.array(mine) == np.array(theirs)).astype(float)
    return round(float((agree * WEIGHTS).sum() / WEIGHTS.sum() * 100))


@app.get("/")
def index():
    return send_from_directory(BASE, "index.html")


@app.post("/api/recommendations")
def recommendations():
    mine = request.json["answers"]
    ranked = [{"id": u["id"], "score": compatibility(mine, u["ans"])} for u in USERS]
    return jsonify(sorted(ranked, key=lambda u: -u["score"]))


if __name__ == "__main__":
    app.run(port=8000, debug=True)
