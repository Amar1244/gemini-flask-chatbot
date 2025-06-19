from flask import Flask, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder=".", static_url_path="")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

@app.route("/")
def serve_frontend():
    return app.send_static_file("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"response": "No prompt provided."}), 400

    response = llm.invoke(prompt)
    return jsonify({"response": response.content})

if __name__ == "__main__":
    app.run(debug=True)
