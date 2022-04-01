from flask import Flask, render_template, request
from utils.dbutils import writeToDb, readFromDb


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def Input():
    return render_template("Input.html")

@app.route('/Homepage', methods=['POST'])
def input():
    word = request.form["word"]
    writeToDb(f"INSERT INTO input_word (name) VALUES ('{word}');")

@app.route('/Homepage', methods=['GET'])
def display():
    heading = ("Word")
    data = readFromDb(f"SELECT * FROM input_word")
    return render_template('/Homepage.html', heading = heading, data = data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)