from flask import Flask, render_template, request, send_file, send_from_directory
import yaml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    with open('data/yates.yml', 'r') as file:
        html_vars = yaml.safe_load(file)
    print(html_vars)  # Debugging line to check the loaded data
    return render_template('resume.html', **html_vars)