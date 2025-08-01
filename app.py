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
def style_var(style):
    html_vars = get_html_vars()
    html_vars['style'] = f'style_{style}.css'
    return render_template('resume.html', **html_vars)

@app.route('/<back_color>/<front_color>')
def style(back_color, front_color):
    html_vars = get_html_vars()
    html_vars['style'] = f'style_var.css'
    html_vars['back_color'] = f'#{back_color}'
    html_vars['front_color'] = f'#{front_color}'
    return render_template('resume.html', **html_vars)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
