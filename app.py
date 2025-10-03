import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-change-me")

VALID_USERNAME = "whiteout"
VALID_PASSWORD = "123"


@app.route("/", methods=["GET", "POST"])  # login
def login():
    if session.get("logged_in"):
        return redirect(url_for("loading"))

    error_message = None

    if request.method == "POST":
        submitted_username = request.form.get("username", "").strip()
        submitted_password = request.form.get("password", "")

        if submitted_username == VALID_USERNAME and submitted_password == VALID_PASSWORD:
            session["logged_in"] = True
            session["username"] = submitted_username
            return redirect(url_for("loading"))
        else:
            error_message = "Invalid username or password"

    return render_template("login.html", error=error_message)


@app.route("/loading", methods=["GET"])  # 5s loading screen then redirect
def loading():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("loading.html")


@app.route("/dashboard", methods=["GET"])  # protected dashboard
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=session.get("username"))


@app.route("/logout", methods=["POST", "GET"])  # simple logout
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), debug=True)
