from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/converter", methods=['POST'])
def convert():
    myDict = {1: 'banana', 2: 'apple', 3: 'protein'}
    key = int(request.form['k'])

    return json.dumps(myDict[key])

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8001)
