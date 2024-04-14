from flask import Blueprint, jsonify, request
from models import Car, db
from helpers import token_required

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/cars', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    car_list = [car.to_dict() for car in cars]
    return jsonify(car_list)

@api.route('/cars/<int:id>', methods=['GET'])
@token_required
def get_car(id):
    car = Car.query.get_or_404(id)
    return jsonify(car.to_dict())

@api.route('/cars', methods=['POST'])
@token_required
def create_car():
    data = request.json
    make = data.get('make')
    model = data.get('model')
    year = data.get('year')

    if not make or not model or not year:
        return jsonify({'error': 'Make, model, and year are required'}), 400

    car = Car(make=make, model=model, year=year)
    db.session.add(car)
    db.session.commit()

    return jsonify(car.to_dict()), 201

@api.route('/cars/<int:id>', methods=['PUT'])
@token_required
def update_car(id):
    car = Car.query.get_or_404(id)
    data = request.json

    # Update only valid fields
    if 'make' in data:
        car.make = data['make']
    if 'model' in data:
        car.model = data['model']
    if 'year' in data:
        car.year = data['year']

    db.session.commit()
    return jsonify(car.to_dict()), 200  # Return 200 status code for successful update

@api.route('/cars/<int:id>', methods=['DELETE'])
@token_required
def delete_car(id):
    car = Car.query.get_or_404(id)
    db.session.delete(car)
    db.session.commit()
    return jsonify(message='Car deleted successfully'), 200  # Return 200 status code for successful delete
