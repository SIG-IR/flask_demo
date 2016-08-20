from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"
    
@app.route("/json")
def json():
    return json.dumps({
        'key': 'value'
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
