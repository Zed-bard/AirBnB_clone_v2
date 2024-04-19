from flask import Flask, render_template, teardown_appcontext
from models import storage, State, City, Amenity, Place

app = Flask(__name__)
app.config[' stric_slashes'] = False

# Function to close SQLAlchemy session after request
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = State.query.order_by(State.name.asc()).all()
    cities = []
    amenities = Amenity.query.order_by(Amenity.name.asc()).all()
    places = Place.query.order_by(Place.name.asc()).all()

    for state in states:
        # Check storage engine type
        if hasattr(state, "cities"):
            cities.extend(state.cities)
        else:
            cities.extend(state.cities())

    # Update template content
    return render_template('100-hbnb.html', states=states, cities=cities, amenities=amenities, places=places)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

