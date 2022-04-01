from flask import Flask, render_template, request, redirect, url_for
from utils.dbutils import writeToDb, readFromDb, updateDb, deleteFromDb


app = Flask(__name__)

@app.route("/")

def home():
    return render_template("Homepage.html")

@app.route('/Homepage', methods=['POST', 'GET'])
def input():
    word = request.form.get("word", False)
    delete_word = request.form.get("delete_word", False)
    update_word = request.form.get("update_word", False)
    id_val_update = request.form.get("id_val_update",False)
    if word:
        writeToDb(f"INSERT INTO input_word (word) VALUES ('{word}');")
    elif update_word:
        updateDb(f"UPDATE input_word SET word = '{update_word}' WHERE id = {id_val_update};")

    elif delete_word:
        deleteFromDb(f"DELETE FROM input_word WHERE word='{delete_word}';")

    # return render_template("/Homepage.html")

    heading = "Word"
    data = readFromDb(f"SELECT * FROM input_word;")
    return render_template('/Homepage.html', heading = heading, data = data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)