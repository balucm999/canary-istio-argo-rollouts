from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! port: 5000</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)