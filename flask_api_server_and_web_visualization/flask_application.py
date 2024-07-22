from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@host:port/database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/Project_3'

db = SQLAlchemy(app)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    latitude = db.Column(db.Numeric(9, 6))
    longitude = db.Column(db.Numeric(9, 6))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/properties')
def get_properties():
    bedrooms = request.args.get('bedrooms', type=int)
    bathrooms = request.args.get('bathrooms', type=int)

    print(f"Endpoint /api/properties - Recieved request - bedrooms[{bedrooms}], bathrooms[{bathrooms}]")

    query = Property.query
    if bedrooms:
        query = query.filter_by(bedrooms=bedrooms)
    if bathrooms:
        query = query.filter_by(bathrooms=bathrooms)

    # Optionally, order the results
    query = query.order_by(desc(Property.id))  # Example ordering by descending property ID

    # properties = query.all()
    #
    # Limit the results to 10 records
    properties = query.limit(10).all()

    print(f"Endpoint /api/properties - SQL Result [{properties}]")

    return jsonify([{
        'name': prop.name,
        'latitude': float(prop.latitude),
        'longitude': float(prop.longitude),
        'bedrooms': prop.bedrooms,
        'bathrooms': prop.bathrooms
    } for prop in properties])

if __name__ == '__main__':
    app.run(debug=True)
