import json
import logging
import os
import sys
from flask import Flask, request, render_template

# Initialize Flask
app = Flask(__name__)

@app.route('/ky', methods=['GET'])
def get_ky():
    return render_template('Kentucky.html')

@app.route('/tn', methods=['GET'])
def get_tn():
    return render_template('Tennessee.html')

@app.route('/tx', methods=['GET'])
def get_tx():
    return render_template('Texas.html')

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

if __name__ == '__main__':
    data_dir = sys.argv[1]
    app.run(host='0.0.0.0', port=5006)
