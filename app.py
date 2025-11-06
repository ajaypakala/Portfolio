from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/internships')
def internships():
    return render_template('internships.html')

@app.route('/ad')
def ad():
    return send_from_directory(os.path.join(app.root_path, 'Certificates'), 'AD-Infocom.pdf')

@app.route('/aws')
def aws():
    return send_from_directory(os.path.join(app.root_path, 'Certificates'), 'AWS AI-ML.pdf')

@app.route('/bp')
def bp():
    return send_from_directory(os.path.join(app.root_path, 'Certificates'), 'Blue prisim.pdf')

@app.route('/resume')
def resume():
    return send_from_directory(os.path.join(app.root_path, 'Certificates'), 'Ajay_Babu_Resume.pdf')

if __name__ == '__main__':
    app.run(debug=True)
