#print("Hello, this Python app is running inside Docker!")

from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello NCC"

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
