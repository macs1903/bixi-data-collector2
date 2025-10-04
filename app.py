from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/bixi/info")
def bixi_info():
    url = "https://gbfs.velobixi.com/gbfs/2-2/fr/station_information.json"
    resp = requests.get(url)
    return jsonify(resp.json())

@app.route("/bixi/status")
def bixi_status():
    url = "https://gbfs.velobixi.com/gbfs/2-2/fr/station_status.json"
    resp = requests.get(url)
    return jsonify(resp.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

