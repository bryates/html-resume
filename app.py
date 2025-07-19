from flask import Flask, render_template, request, send_file, send_from_directory
import yaml

app = Flask(__name__)

def get_html_vars():
    with open('data/yates.yml', 'r') as file:
        html_vars = yaml.safe_load(file)
    html_vars['style'] = 'style.css'
    return html_vars

@app.route('/', methods=['GET', 'POST'])
def index():
    html_vars = get_html_vars()
    return render_template('resume.html', **html_vars)

@app.route('/<style>')
def style(style):
    with open('data/yates.yml', 'r') as file:
        html_vars = yaml.safe_load(file)
    html_vars = get_html_vars()
    html_vars['style'] = f'style_{style}.css'
    return render_template('resume.html', **html_vars)

if __name__ == '__main__':
    app.run(debug=True)
