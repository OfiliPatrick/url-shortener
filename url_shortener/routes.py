"""A module containing API endpoints and routes """

from flask import Blueprint, render_template, request, redirect
from validators import url
from .extensions import db
from .models import Url


shortener = Blueprint('shortener', __name__)
@shortener.route("/")
def index():
    """Returns Shrinkly homepage
    """
    return render_template("index.html")

@shortener.route("/add_url", methods=["POST"])
def add_url():
    """Handles URL Submissions and returns submission info
    """
    original_url = request.form["original_url"]
    if not url(original_url):
        return render_template("error.html", error="Invalid URL, enter a valid URL.")
    new_url = Url(original_url=original_url)
    db.session.add(new_url)
    db.session.commit()
    return render_template("url_added.html", original_url=original_url,
    short_url=new_url.short_url)

@shortener.route("/<query_short_url>")
def redirect_to_original_url(query_short_url):
    """ Redirects shortened URL to original URL"""
    db_url = Url.query.filter_by(short_url=query_short_url).first_or_404()
    db_url.views += 1
    db.session.commit()
    return redirect(db_url.original_url)


@shortener.errorhandler(404)
def page_not_found(error):
    """Handles unregistered routes and returns 404 page"""
    return '<h1> 404 - Not Found</h1>', 404
