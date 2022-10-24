from api.v1.views.index import *
from models.review import Review
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models import storage
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
