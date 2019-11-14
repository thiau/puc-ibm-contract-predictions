from flask import Flask, jsonify
from app.helpers.transformations import add_number

app = Flask(__name__)