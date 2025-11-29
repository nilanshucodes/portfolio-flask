
from flask import Flask, render_template, send_from_directory, url_for
import json, os

app = Flask(__name__)

def load_profile():
    data_path = os.path.join(app.root_path, "data", "profile.json")
    with open(data_path, "r") as f:
        return json.load(f)

@app.route("/")
def index():
    profile = load_profile()
    return render_template("index.html", profile=profile)

@app.route("/projects")
def projects():
    profile = load_profile()
    return render_template("projects.html", profile=profile)

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/download/resume")
def download_resume():
    return send_from_directory(directory="resume", path="Nilanshu_RESUME_232.pdf", as_attachment=True)

@app.errorhandler(404)
def not_found(e):
    profile = load_profile()
    return render_template("404.html", profile=profile), 404


