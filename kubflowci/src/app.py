import socket
from uuid import getnode as get_mac
from flask import Flask, jsonify, render_template

# Get pod details
def get_pod_details():
    hostname = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    mac_address = get_mac()
    mac_address = (':'.join(("%012X" % mac_address)[i:i+2] for i in range(0, 12, 2))).replace(":", "-")
    return hostname, ip, mac_address

app = Flask(__name__)

# Returns pod hostname, IP, and MAC address
@app.route("/details")
def details():
    hostname, ip, mac = get_pod_details()
    return render_template("details.html", hostname=hostname, ip=ip, mac=mac)

@app.route("/health")
def health():
    return jsonify(status="up")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
