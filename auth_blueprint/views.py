from flask import (
    render_template,
    request,
    redirect,
    session,
    current_app,
    flash,
)
from auth_blueprint import auth_blueprint
import mysql.connector
import bcrypt
from geopy.geocoders import Nominatim
import folium


# Halaman utama (register dan login)
@auth_blueprint.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        success, message = register_user(username, password)
        if success:
            flash(message, "success")
            return redirect("/login")
        else:
            flash(message, "error")
    return render_template("register.html")


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
        # Mendapatkan lokasi menggunakan geopy
        geolocator = Nominatim(user_agent='myapp')
        location = geolocator.geocode('London, UK')

        # Mendapatkan koordinat latitude dan longitude
        lat = location.latitude
        lon = location.longitude

        # Membuat peta menggunakan folium
        m = folium.Map(location=[lat, lon], zoom_start=12)

        # Menambahkan penanda pada peta
        folium.Marker([lat, lon], popup='Lokasi saat ini').add_to(m)

        # Mengubah peta menjadi file HTML
        m.save('map.html')
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

    query_check_username = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query_check_username, (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        return False, "Username sudah ada"

    salt = bcrypt.gensalt().decode("utf-8")
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt.encode("utf-8"))
    query = "INSERT INTO users (username, password, salt) VALUES (%s, %s, %s)"
    values = (username, hashed_password.decode("utf-8"), salt)
    cursor.execute(query, values)
    db.commit()
    cursor.close()

    return True, "Berhasil Daftar"


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
