# 0. Import Flask and render template
from flask import Flask, render_template

# 1. Set up Flask app
app = Flask(__name__)

# 2. Set up routes
@app.route("/")

# 3. Set up main method - return - render template of index.html
def main():
    return render_template("index.html")

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

# 4. Run the server with main method
if __name__ == "__main__":
    app.run()