
# main.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/donation_matching')
def donation_matching():
    return render_template('donation_matching.html')

@app.route('/submit', methods=['POST'])
def submit():
    linkedin_url = request.form['linkedin_url']
    email = request.form['email']

    # Validate the information
    if not linkedin_url or not email:
        return redirect(url_for('error'))

    # Send the information to the database or API

    return redirect(url_for('success'))

if __name__ == '__main__':
    app.run(debug=True)
