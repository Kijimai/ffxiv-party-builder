from flask import render_template, redirect, request, session, flash
from flask_app import app
import asyncio
import logging
import pyxivapi
import aiohttp

from pyxivapi.models import Filter, Sort

# import models here

def fetchCharacter(id):
    return


@app.route('/')
def render_index():
    return redirect('/login-registration')


@app.route('/login-registration')
def render_login_registration():
    return render_template('login_register.html')


@app.route('/dashboard')
def render_dashboard():
    return render_template('dashboard.html')


@app.route('/welcome')
def render_welcome():
    return render_template('welcome.html')


@app.route('/welcome_character', methods=['POST'])
def choose_character():
    print(request.form)
    return redirect('/dashboard')


@app.route('/characters/<int:id>')
def show_one_character(id):
    return render_template('show_one_party_member.html', character=fetchCharacter(id))
