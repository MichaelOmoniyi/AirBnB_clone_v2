#!/usr/bin/python3
"""A script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /states_list: display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present
            in DBStorage sorted by name (A->Z) tip
                LI tag: description of one
                State: <state.id>: <B><state.name></B>
"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """
        display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present
            in DBStorage sorted by name (A->Z) tip
            LI tag: description of one
            State: <state.id>: <B><state.name></B>
    """

    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(exc):
    """ Removes the current SQLAlchemy Session """

    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """
        display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present
            in DBStorage sorted by name (A->Z) tip
                LI tag: description of one State: <state.id>:
                <B><state.name></B> + UL tag: with the list of
                City objects linked to the State sorted by name (A->Z)
                    LI tag: description of one
                    City: <city.id>: <B><city.name></B>
    """

    states = storage.all("State")
    cities = storage.all("Cities")
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


@app.route('/states/<id>', strict_slashes=False)
def states_id(state_id):
    """
        display a HTML page: (inside the tag BODY)
        If a State object is found with this id:
            H1 tag: “State: ”
            H3 tag: “Cities:”
            UL tag: with the list of City objects linked
            to the State sorted by name (A->Z)
                LI tag: description of one City:
                <city.id>: <B><city.name></B>
        Otherwise:
            H1 tag: “Not found!”
    """

    states = storage.all("State")
    return render_template('9-states.html', state_id=id,
                           states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
