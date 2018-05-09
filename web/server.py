from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', message="Hey!")

@app.route("/update", methods=["POST"])
def update_script():
    pass

@app.route("/upload", methods=["POST"])
def upload_new_script():
    pass

@app.route("/run", methods=["POST"])
def run_script():
    pass


if __name__ == "__main__":  
    app.run(debug=True)