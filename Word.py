from flask import Flask, render_template, request
from utils.dbutils import writeToDb, readFromDb, updateDb, deleteFromDb


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def Input():
    return render_template("Input.html")

@app.route('/Homepage', methods=['POST'])
def input():
    word = request.form["word"]
    delete_word = request.form["delete_word"]
    update_word = request.form["update_word"]
    id_val_update = request.form["id_val_update"]
    if word:
        writeToDb(f"INSERT INTO input_word (name) VALUES ('{word}');")
    if update_word:
        updateDb(f"UPDATE input_word SET word = '{update_word}' WHERE id = {id_val_update};")

    if delete_word:
        deleteFromDb(f"DELETE FROM input_word WHERE word = '{delete_word}'; ")

@app.route('/Homepage', methods=['GET'])
def display():
    heading = ("Word")
    data = readFromDb(f"SELECT * FROM input_word;")
    return render_template('/Homepage.html', heading = heading, data = data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)