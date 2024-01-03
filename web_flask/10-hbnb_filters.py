#!/usr/bin/python3
"""A script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /states_list: display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present
            in DBStorage sorted by name (A->Z) tip
                LI tag: description of one State:
                <state.id>: <B><state.name></B>
"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ display a HTML page like 6-index.html """

    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def close(exc):
    """ Removes the current SQLAlchemy Session """

    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
