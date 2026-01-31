from flask import Flask, request, jsonify
from flask_cors import CORS
from ai import trip_ai

app = Flask(__name__)
CORS(app)

@app.route("/plan", methods=["POST"])
def plan():
    data = request.json
    user_prompt = f"""
    You are a travel AI.
    Destination: {data['city']}
    Budget: {data['budget']}
    Days: {data['days']}
    Mood: {data['mood']}
    Generate a full travel plan.
    """
    result = trip_ai(user_prompt)
    return jsonify({"reply": result})

app.run(host="0.0.0.0", port=10000)
