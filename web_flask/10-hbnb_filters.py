#!/usr/bin/python3
"""Flask module"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    print(amenities)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)

@app.teardown_appcontext
def storage_close(exception):
    """Teardown"""
    storage.close()

if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000', debug=True)