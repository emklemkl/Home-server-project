#!/usr/bin/env python3
from flask import Flask, render_template, request, url_for, redirect
from src.helper import Helper
from src.database import Database

app = Flask(__name__)
db = Database()

@app.route("/")
def start_page():
    return render_template("base.html.j2", _path=Helper.template_selector())

@app.route("/projects")
def projects_page():
    projects_list = db.get_doc_in_collection_names("projects")
    print(projects_list)
    return render_template("base.html.j2", _path=Helper.template_selector(), projects=projects_list)

@app.route("/project/<project_id>")
def project_page(project_id):
    project_list = db.get_doc_based_on_id("projects", project_id)
    print(project_list)
    print(type(project_list),"<- Type")
    return render_template("base.html.j2", _path=Helper.template_selector(project_id), project=project_list)

@app.route("/receipts")
def receipts_page():
    project_list = db.get_doc_in_collection_names("projects")
    return render_template("base.html.j2", _path=Helper.template_selector(), projects=project_list)

@app.errorhandler(404) 
def not_found(e):
    print(e) 
    return redirect(url_for("start_page")) 

if __name__ == "__main__":
    # project_page("6661982f72f0ee3f3bdb83b0")
    app.run(debug=True)