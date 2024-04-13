from flask import Blueprint, request, jsonify
from flask_login import login_required
from models import Car, db  # Import your Car model and database instance

cars_bp = Blueprint('cars', __name__)

@cars_bp.route('/cars', methods=['POST'])
@login_required
def create_car():
    data = request.get_json()
    make = data.get('make')
    model = data.get('model')
    year = data.get('year')

    new_car = Car(make=make, model=model, year=year)
    db.session.add(new_car)
    db.session.commit()

    return jsonify({'message': 'Car created successfully', 'car': new_car.to_dict()}), 201

@cars_bp.route('/cars', methods=['GET'])
@login_required
def get_all_cars():
    cars = Car.query.all()
    cars_list = [car.to_dict() for car in cars]
    return jsonify(cars_list)

@cars_bp.route('/cars/<int:car_id>', methods=['GET'])
@login_required
def get_car(car_id):
    car = Car.query.get_or_404(car_id)
    return jsonify(car.to_dict())

@cars_bp.route('/cars/<int:car_id>', methods=['PUT'])
@login_required
def update_car(car_id):
    car = Car.query.get_or_404(car_id)
    data = request.get_json()
    car.make = data.get('make', car.make)
    car.model = data.get('model', car.model)
    car.year = data.get('year', car.year)
    db.session.commit()
    return jsonify({'message': 'Car updated successfully', 'car': car.to_dict()})

@cars_bp.route('/cars/<int:car_id>', methods=['DELETE'])
@login_required
def delete_car(car_id):
    car = Car.query.get_or_404(car_id)
    db.session.delete(car)
    db.session.commit()
    return jsonify({'message': 'Car deleted successfully'})
