from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello Ahmad! Python Flask is running from AWS Singapore"
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
