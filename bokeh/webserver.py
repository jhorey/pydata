import json
import logging
import os
import sys
from flask import Flask, request, render_template

# Initialize Flask
app = Flask(__name__)

@app.route('/ky', methods=['GET'])
def get_ky():
    print "kentucky"
    return render_template('Kentucky.html')

@app.route('/tn', methods=['GET'])
def get_tn():
    print "tennessee"
    return render_template('Tennessee.html')

@app.route('/tx', methods=['GET'])
def get_tx():
    print "texas"
    return render_template('Texas.html')

@app.route('/', methods=['GET'])
def get_index():
    print "index"
    return render_template('index.html')

if __name__ == '__main__':
    data_dir = sys.argv[1]
    app.run(host='0.0.0.0', port=8000)
