from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# dynamic route

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login')
def home_page():
    return render_template('login.html')

@app.route('/signup')
def home():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/privacyterms')
def privacyterms():
    return render_template('privacyterms.html')

if __name__ == "__main__":
    app.run(debug=True)