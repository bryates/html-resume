from flask import Flask, render_template, request, send_file, send_from_directory
import json
import random
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('resume.html')