from flask import Blueprint, render_template
from flask_login import login_required, current_user

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template("index.html")

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

# Add the route for the car inventory page here
@site.route('/car_inventory')
def car_inventory():
    # Add your logic to display the car inventory page
    return render_template("car_inventory.html")
