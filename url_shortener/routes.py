from flask import Blueprint, render_template, request
from .extensions import db
from .models import Url

shortener = Blueprint('shortener', __name__)

@shortener.route("/")
def index():
    return render_template("index.html")

@shortener.route("/add_url", methods = ["POST"])
def add_url():
    original_url = request.form["original_url"]
    new_url = Url(original_url=original_url)
    db.session.add(new_url)
    db.session.commit()
  
    return render_template("url_added.html", original_url= original_url, short_url = new_url.short_url )

@shortener.route("/views")
def views():
    pass


@shortener.route("/error_handler")
def error_handler():
    pass

