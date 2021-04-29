#!/usr/bin/python3
"""Flask module"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Main page rout"""
    data = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=data)

@app.teardown_appcontext
def storage_close(exception):
    """Teardown"""
    storage.close()

if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000', debug=True)
