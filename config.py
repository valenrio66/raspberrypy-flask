from flask_uploads import UploadSet, IMAGES, VIDEOS

DATABASE_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "dbrasp",
}

# Inisialisasi objek UploadSet
photos = UploadSet('photos', IMAGES)
videos = UploadSet('videos', VIDEOS)