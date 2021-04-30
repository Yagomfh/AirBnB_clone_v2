#!/usr/bin/python3
"""Flask module"""
from flask import Flask, render_template
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    users = storage.all(User)
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities,
                           places=places, users=users)


@app.teardown_appcontext
def storage_close(exception):
    """Teardown"""
    storage.close()

if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000', debug=True)