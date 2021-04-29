#!/usr/bin/python3
"""Flask module"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """states id route"""
    states = storage.all(State).values()
    if id is None:
        return render_template('9-states.html', states=states, id=id)
    states = storage.all(State)
    state_id = 'State.' + id
    if state_id in states:
        data = []
        data.append(states[state_id].name)
        data.append(id)
        Cs = []
        for city in states[state_id].cities:
            Cs.append(city)
        data.append(Cs)
        return render_template('9-states.html', states=data, id=id)
    else:
        return render_template('9-states.html', states=states, id='Not found')


@app.teardown_appcontext
def storage_close(exception):
    """Teardown"""
    storage.close()

if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000', debug=True)
