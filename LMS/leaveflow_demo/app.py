from flask import (
    Flask, render_template, request,
    redirect, url_for, session
)

import os

app = Flask(__name__)

app.secret_key = os.environ["SECRET_KEY"]

users = {
    "employee": {"password": "emp123", "role": "employee"},
    "manager": {"password": "mng123", "role": "manager"},
    "admin": {"password": "admin", "role": "admin"}
}

@app.route("/")

def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
                              
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = users.get(username)

        if user and user["password"] == password:
            session.clear()
            session["username"] = username
            session["role"] = user["role"]

            return redirect(url_for(user["role"]))

        error = "Invalid username or password"

    return render_template("login.html", error=error)

@app.route("/employee")
def employee():
    if session.get("role") != "employee":
        return redirect(url_for("login"))

    return render_template("employee.html")

@app.route("/manager")
def manager():
    if session.get("role") != "manager":
        return redirect(url_for("login"))

    return render_template("manager.html")

@app.route("/admin")
def admin():
    if session.get("role") != "admin":
        return redirect(url_for("login"))

    return render_template("admin.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)