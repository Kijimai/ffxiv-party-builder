from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app import API_KEY
from flask_app.models.user import User
from flask_app.models.character import Character
import asyncio
import logging
import pyxivapi
import aiohttp
from pyxivapi.models import Filter, Sort
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# import models here


def fetchCharacter(id):
    return


@app.route('/')
def render_index():
    if session.get('id'):
        return redirect('/dashboard')
    return redirect('/login-registration')


@app.route('/login-registration')
def render_login_registration():
    return render_template('login_register.html')


@app.route('/register_user', methods=["POST"])
def register_user():
    if request.form['username'] == '':
        flash('Please enter a valid last name!', 'err_user_register_username')
        return redirect('/')

    elif len(request.form['username']) < 4:
        flash('Last name must be longer than 4 characters!',
              'err_user_register_username')
        return redirect('/')

    elif not request.form['password']:
        flash('Please enter a valid password!',
              'err_user_register_password')
        return redirect('/')

    elif len(request.form['password']) < 8:
        flash('Password must be at least 8 characters long!',
              'err_user_register_password')
        return redirect('/')
    if not User.validate_email({"email": request.form["email"]}) or not User.validate_unique_email({"email": request.form["email"]}):
        return redirect('/')

    data = {
        "username": request.form["username"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"])
    }
    id = User.save(data)
    session['id'] = id
    return redirect('/dashboard')


@app.route('/login_user', methods=["POST"])
def login_user():
    if request.form['email'] == '':
        flash('You must enter an email to log in.', 'err_user_login_email')
        return redirect('/')
    elif request.form['password'] == '':
        flash('You must enter a password to log in.', 'err_user_login_password')
        return redirect('/')
    data = {
        "email": request.form['email']
    }
    user_in_db = User.get_user_by_email(data)
    if not user_in_db:
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        return redirect('/')
    session['id'] = user_in_db.id
    return redirect('/dashboard')


@app.route('/logout')
def logout_user():
    if session.get('id'):
        del session['id']
    return redirect('/')


@app.route('/dashboard')
def render_dashboard():
    if not session.get('id'):
        flash('You do not have permission to view the dashboard page. Please login first!',
              'err_user_unauthorized')
        return redirect('/')
    # return render_template('dashboard.html')
    return render_template('dashboard.html', currentUser=User.get_user({"id": session["id"]}))


@app.route('/welcome')
def render_welcome():
    return render_template('welcome.html')


@app.route('/welcome_character', methods=['POST'])
def choose_character():
    print(request.form)
    return redirect('/dashboard')


# todo: change up 1
# @app.route('/characters/1')
# def show_one_character():
#     return render_template('show_one_party_member.html', API_KEY=API_KEY)

@app.route('/characters/<int:id>')
def show_one_character(id):
    return render_template('show_one_party_member.html', characterID=id)


@app.route('/search_characters')
def render_search_characters():
    return render_template('search_characters.html')


@app.route('/add_to_party', methods=["POST"])
def add_to_party():
    print(request.form)
    id = Character.save(request.form)
    print(id)
    return redirect('/dashboard')


@app.route('/update_user_character', methods=["POST"])
def update_user_character():
    print("************************")
    print('updating user character!')
    print("************************")
    return request.form
