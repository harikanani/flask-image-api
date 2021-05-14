from flask_cors import CORS
from flask import Flask, jsonify
import os

# print(os.getcwd())
os.chdir("./static/img")

# print(os.getcwd())
# print(os.listdir())


app = Flask(__name__)
CORS(app)


@app.route("/get-images", methods=['GET'])
def hello():
    return jsonify(os.listdir()), 200


if __name__ == "__main__":
    app.run(debug=True)
