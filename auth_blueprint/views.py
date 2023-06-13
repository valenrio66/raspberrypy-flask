from flask import (
    render_template,
    request,
    redirect,
    session,
    current_app,
    flash,
    url_for
)
from auth_blueprint import auth_blueprint
import mysql.connector
import bcrypt
from config import photos, videos


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
        return render_template("dashboard.html", username=username)
    else:
        return redirect("/login")


@auth_blueprint.route("/dashboard/tables")
def tables():
    return render_template("tables.html")


@auth_blueprint.route("/dashboard/albumfoto")
def foto():
    return render_template("albumfoto.html")


@auth_blueprint.route("/dashboard/albumvideo")
def video():
    return render_template("albumvideo.html")


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

@auth_blueprint.route('/upload-photo', methods=['GET', 'POST'])
def upload_photo():
    if request.method == 'POST' and 'photo' in request.files:
        photo = request.files['photo']
        filename = photos.save(photo)
        # Simpan informasi file ke database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO photos (filename) VALUES (%s)", (filename,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('upload_photo.html')

@auth_blueprint.route('/upload-video', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST' and 'video' in request.files:
        video = request.files['video']
        filename = videos.save(video)
        # Simpan informasi file ke database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO videos (filename) VALUES (%s)", (filename,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('upload_video.html')