from flask import Flask
from auth_blueprint import auth_blueprint
from config import DATABASE_CONFIG

app = Flask(__name__)
app.secret_key = "secret_key"
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mkv'}


# Konfigurasi database
app.config["DATABASE_CONFIG"] = DATABASE_CONFIG

# Daftarkan blueprint
app.register_blueprint(auth_blueprint)

# Fungsi untuk memeriksa apakah ekstensi file diizinkan
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
