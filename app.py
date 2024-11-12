from flask import Flask, request, jsonify
import random
import os

app = Flask(__name__)

# Route_student number
@app.route('/', methods=['GET'])
def student_info():
    return jsonify({"student_number": "200561609"})

# Webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    intent_name = req.get("queryResult").get("intent").get("displayName")
    joke_type = req.get("queryResult").get("parameters").get("joke_type")

    #response
    if intent_name == "Tell a Joke":
        jokes = {
            "math joke": [
                "Why did the math book look sad? Because it had too many problems.",
                "Parallel lines have so much in common… it’s a shame they’ll never meet!"
            ],
            "tech joke": [
                "I told my computer I needed a break, and now it won’t stop sending me cookies.",
                "Why do programmers prefer dark mode? Because the light attracts bugs!"
            ],
            "random joke": [
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "I asked my dog what’s two minus two. He said nothing."
            ]
        }
        #joke based on joke type
        response_text = random.choice(jokes.get(joke_type.lower(), jokes["random joke"]))
    else:
        response_text = "I'm here to assist you!"

    # Return fulfillment response to Dialogflow
    return jsonify({"fulfillmentText": response_text})

if __name__ == '__main__':
app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
