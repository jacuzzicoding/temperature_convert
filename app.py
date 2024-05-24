from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello, welcome to the temperature converter!"

if __name__ == "__main__":
    app.run(debug=True)