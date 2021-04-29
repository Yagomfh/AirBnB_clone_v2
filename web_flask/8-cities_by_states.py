#!/usr/bin/python3
"""Flask module"""
from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """Main page rout"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    data = []
    for state in states:
        tmp = {}
        tmp['state'] = state
        l = []
        for city in cities:
            if city.state_id == state.id:
                l.append(city)
        tmp['cities'] = l
        data.append(tmp)
    return render_template('8-cities_by_states.html', data=data)

@app.teardown_appcontext
def storage_close(exception):
    """Teardown"""
    storage.close()

if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000', debug=True)
