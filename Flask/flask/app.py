from flask import Flask, render_template


###WSGI application
app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to this Flask course Hehehehehe"

@app.route("/index")
def index_page():
    return render_template('index.html')

if __name__== "__main__":
    app.run(debug=True)
