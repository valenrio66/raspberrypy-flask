from flask import Flask
from auth_blueprint import auth_blueprint
from config import DATABASE_CONFIG

app = Flask(__name__)
app.secret_key = "secret_key"

# Konfigurasi database
app.config["DATABASE_CONFIG"] = DATABASE_CONFIG

# Daftarkan blueprint
app.register_blueprint(auth_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
