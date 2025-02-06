from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Homepage Route
@app.route('/')
def home():
    return render_template('index.html')

# About Page Route
@app.route('/about')
def about():
    return render_template('about.html')

# Form Submission Route
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('thank_you', name=name))

# Thank You Page Route
@app.route('/thank_you/<name>')
def thank_you(name):
    return f"Thank you, {name}!"

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
