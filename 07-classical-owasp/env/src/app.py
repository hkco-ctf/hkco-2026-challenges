from flask import Flask, request, render_template
import sqlite3
import os
import secrets

FLAG = os.getenv("FLAG", "hkco2026{this_is_a_dummy_flag}")

app = Flask(__name__)

db = sqlite3.connect(":memory:", check_same_thread=False)
db.execute(
    "CREATE TABLE users ("
    "id INTEGER PRIMARY KEY, "
    "username TEXT, "
    "password TEXT, "
    "is_admin INTEGER)"
)
db.execute(
    "INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)",
    ("admin", secrets.token_hex(32), 1),
)
db.execute(
    "INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)",
    ("guest", "guest", 0),
)
db.commit()


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    status = ""
    flag = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        query = (
            "SELECT username, is_admin FROM users "
            "WHERE username='" + username + "' "
            "AND password='" + password + "'"
        )
        try:
            row = db.execute(query).fetchone()
        except sqlite3.Error as e:
            return render_template(
                "index.html", message=f"SQL error: {e}", status="err", flag=""
            )
        if row is None:
            message = "Invalid credentials."
            status = "err"
        else:
            user, is_admin = row
            if is_admin:
                message = f"Welcome, {user}. Here is your flag:"
                status = "ok"
                flag = FLAG
            else:
                message = f"Welcome, {user}. Nothing interesting here."
                status = "info"
    return render_template("index.html", message=message, status=status, flag=flag)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)
