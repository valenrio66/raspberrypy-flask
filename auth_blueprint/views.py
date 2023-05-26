from flask import render_template, request, redirect, session, current_app
from auth_blueprint import auth_blueprint
import mysql.connector
import bcrypt


# Halaman utama (register dan login)
@auth_blueprint.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Panggil fungsi register
        register_user(username, password)
        return redirect("/login")
    return render_template("index.html")


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Panggil fungsi login
        if login_user(username, password):
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Invalid username or password.")
    return render_template("login.html")


# Halaman dashboard setelah login
@auth_blueprint.route("/dashboard")
def dashboard():
    if "username" in session:
        username = session["username"]
        return render_template("dashboard.html", username=username)
    else:
        return redirect("/login")


# Halaman logout
@auth_blueprint.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")


# Fungsi untuk registrasi pengguna
def register_user(username, password):
    db = mysql.connector.connect(**current_app.config["DATABASE_CONFIG"])
    cursor = db.cursor()
    salt = bcrypt.gensalt().decode("utf-8")
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt.encode("utf-8"))
    query = "INSERT INTO users (username, password, salt) VALUES (%s, %s, %s)"
    values = (username, hashed_password.decode("utf-8"), salt)
    cursor.execute(query, values)
    db.commit()
    cursor.close()


# Fungsi untuk login pengguna
def login_user(username, password):
    db = mysql.connector.connect(**current_app.config["DATABASE_CONFIG"])
    cursor = db.cursor()
    query = "SELECT password, salt FROM users WHERE username = %s"
    values = (username,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    if result:
        stored_password = result[0].encode("utf-8")
        stored_salt = result[1].encode("utf-8")
        if bcrypt.checkpw(password.encode("utf-8"), stored_password):
            session["username"] = username
            return True
    return False
