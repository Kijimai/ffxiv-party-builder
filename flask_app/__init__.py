from flask import Flask
from decouple import config

API_KEY = config('FFXIV_API_KEY')
app = Flask(__name__)
app.secret_key = 'mysupersecretkey'
