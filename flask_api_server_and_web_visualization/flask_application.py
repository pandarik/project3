from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@host:port/database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/Project_3'

db = SQLAlchemy(app)

class Property(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(255))
    latitude    = db.Column(db.Numeric(9, 6))
    longitude   = db.Column(db.Numeric(9, 6))
    bedrooms    = db.Column(db.Integer)
    bathrooms   = db.Column(db.Integer)
    price       = db.Column(db.Integer) 
    rating      = db.Column(db.String)
    rating_desc = db.Column(db.String)
    num_reviews = db.Column(db.String)
    num_people  = db.Column(db.Integer)
    destination = db.Column(db.String)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/properties')
def get_properties():
    bedrooms    = request.args.get('bedrooms' , type=int)
    bathrooms   = request.args.get('bathrooms', type=int)
    min_price   = request.args.get('min_price', type=int)
    max_price   = request.args.get('max_price', type=int)
    destination = request.args.get('destination')

    query = Property.query
    if bedrooms:
        query = query.filter_by(bedrooms=bedrooms)
    if bathrooms:
        query = query.filter_by(bathrooms=bathrooms)
    if min_price:
        query = query.filter(Property.price >= min_price)
    if max_price:
        query = query.filter(Property.price <= max_price)
    if destination:
        query = query.filter_by(destination=destination)

    # Optionally, order the results
    query = query.order_by(desc(Property.id))  # Example ordering by descending property ID
    # query = query.order_by(desc(Property.rating))  # Example ordering by highest rating
    # query = query.order_by((Property.rating))  # Example ordering by lowest rating

    # properties = query.all()
    #
    # Limit the results to 25 records
    properties = query.limit(25).all()

    # print(f"Endpoint /api/properties - SQL Result [{properties}]")

    return jsonify([{
        'name':        prop.name,
        'latitude':    float(prop.latitude),
        'longitude':   float(prop.longitude),
        'bedrooms':    prop.bedrooms,
        'bathrooms':   prop.bathrooms,
        'price':       prop.price,
        'rating':      prop.rating,
        'rating_desc': prop.rating_desc,
        'num_reviews': prop.num_reviews,
        'num_people':  prop.num_people,
        'destination': prop.destination
    } for prop in properties])

@app.route('/api/destinations')
def get_destinations():
    destinations = db.session.query(Property.destination).distinct().all()
    return jsonify([
        dest[0] for dest in destinations if dest[0]
    ])

if __name__ == '__main__':
    app.run(debug=True)
