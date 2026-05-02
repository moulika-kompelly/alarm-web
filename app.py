from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

FILE = "alarms.json"

def load_alarms():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_alarms(alarms):
    with open(FILE, "w") as f:
        json.dump(alarms, f)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get_alarms")
def get_alarms():
    return jsonify(load_alarms())

@app.route("/add_alarm", methods=["POST"])
def add_alarm():
    time = request.json.get("time")
    alarms = load_alarms()
    alarms.append(time)
    save_alarms(alarms)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)