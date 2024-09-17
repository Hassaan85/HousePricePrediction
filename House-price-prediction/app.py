from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    val1 = request.form['bedrooms']
    val2 = request.form['bathrooms']
    val3 = request.form['floors']
    val4 = request.form['yr_built']
    arr = np.array([val1, val2, val3, val4])
    arr = arr.astype(np.float64)
    pred = model.predict([arr])

    return render_template('index.html', data=int(pred))

# Route for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        # You should handle user creation logic here, such as saving to a database
        # For now, just redirect to the main page
        return redirect(url_for('index'))
    return render_template('signup.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # You should validate login credentials here
        # For now, just redirect to the main page
        return redirect(url_for('index'))
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
