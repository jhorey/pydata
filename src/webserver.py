import json
import logging
from flask import Flask, request, render_template

# Initialize Flask
app = Flask(__name__)

@app.route('/econ', methods=['GET'])
def get_econ_page():
    return render_template('/home/ferry/pydata/geospatial.html')
