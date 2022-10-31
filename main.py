from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return jsonify({"Mensagem": "Daniel a"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
