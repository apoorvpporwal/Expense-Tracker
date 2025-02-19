from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        amount REAL NOT NULL,
                        category TEXT NOT NULL,
                        description TEXT,
                        date TEXT NOT NULL)''')
    conn.commit()
    conn.close()

init_db()


@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    expenses = cursor.fetchall()
    conn.close()
    return render_template("index.html", expenses=expenses)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        amount = request.form["amount"]
        category = request.form["category"]
        description = request.form["description"]
        date = request.form["date"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                       (amount, category, description, date))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
