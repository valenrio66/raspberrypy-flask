from flask import Blueprint

auth_blueprint = Blueprint("auth_blueprint", __name__)

# Import views dari blueprint
from auth_blueprint import views
