# 0. Import Flask, render template, json and request (to read POSTed values)
from flask import Flask, render_template, json, request

# 1. Set up Flask app
app = Flask(__name__)

# 2. Set up routes
@app.route("/")

# 3. Set up main method - return -> render template of index.html
def main():
    return render_template("index.html")

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods = ['POST'])
def signUp():
    
    # Read the posted values from UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # Validates the received values
    if _name and _email and _password:
        return json.dumps({'html': '<span>All fields good!!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields.</span>'})

# 4. Run the server with main method
if __name__ == "__main__":
    app.run()