"""Server for Travel App"""

from flask import Flask, jsonify, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
import APIfunctions
import os
from jinja2 import StrictUndefined


app = Flask(__name__)

SECRET_KEY = os.environ['SECRET_KEY']
app.secret_key = SECRET_KEY


@app.route('/')
def display_homepage():
    """Show the homepage"""

    return render_template('index.html')


@app.route('/api/login-user', methods=['POST'])
def log_in_user():
    """Log in user"""

    email = request.form.get('login-email')
    password = request.form.get('login-password')

    user = crud.find_user_by_email(email)
    user_password = user.check_password(password)

    #verifies that user email and password match what is in database
    if user.email == email and user_password == True:
        session['user'] = user.id
        flash('Successfully logged in!')
    
    else:
        flash('Unable to login, please try again')

    return redirect('/')

@app.route('/api/create-account', methods=['POST'])
def create_new_account():
    """Create a new account"""

    username = request.form.get('new-username')
    email = request.form.get('new-email')
    password = request.form.get('new-password')
    fname = request.form.get('new-fname')
    lname = request.form.get('new-lname')

    #checks if user is already in database
    user = crud.find_user_by_email(email)
    
    #if user not already in database, create new user
    if user == None:
        user = crud.create_user(username, email, password, fname, lname)
        session['user'] = user.id
        flash('Successfully created account and logged in.')
    
    else:
        flash('Unable to create account with that email.')
        
    return redirect('/')


@app.route('/api/destination')
def show_user_places():
    """Display places for searched destination"""

    print('THIS SEARCH FUNCTION IS BEING CALLED')
    print('*' * 100)
    place = request.args.get('search_input')
    print('place', place)

    location_coord = APIfunctions.get_place_coordinates(place)
    print('coords', location_coord)
    poi_options = APIfunctions.get_points_of_interests(location_coord)
    print('poi_opts', poi_options)
    poi_details = APIfunctions.get_place_info(poi_options)
    print(poi_details)

    print('*' * 100)
    print('details', poi_details)
    print('*' * 100)

    return jsonify({'places': poi_details})




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', port='5757', debug=True)