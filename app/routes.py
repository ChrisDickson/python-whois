from app import app
from flask import render_template, request, jsonify
from whois import whois
import json
@app.route('/')
def whois_index():
    return render_template("whois.html", title="whois")

@app.route('/', methods=['POST'])
def whois_post():
    domain = request.form['domain']
    w = whois(domain)
    w_json = json.loads(str(w))
    w = json.dumps(w_json, indent=4)
    return render_template("whois.html", whois_info=w)