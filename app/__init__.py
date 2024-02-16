from flask import Flask, jsonify, request
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ml_api.db'
db = SQLAlchemy(app)

from app import routes

