from flask import Blueprint, render_template, request, redirect
from .extensions import db
from .models import Url
from .auth import requires_auth

shortener = Blueprint('shortener', __name__)

@shortener.route("/")
@requires_auth
def index():
    return render_template("index.html")


@shortener.route("/add_url", methods=["POST"])
@requires_auth
def add_url():
    original_url = request.form["original_url"]
    new_url = Url(original_url=original_url)
    db.session.add(new_url)
    db.session.commit()
    return render_template("url_added.html", original_url= original_url, short_url = new_url.short_url )


@shortener.route("/<query_short_url>")
def redirect_to_original_url(query_short_url):
    db_url = Url.query.filter_by(short_url=query_short_url).first_or_404()
    db_url.views += 1
    db.session.commit()
    return redirect(db_url.original_url)


@shortener.route("/views")
@requires_auth
def views():
    urls = Url.query.all()
    return render_template("view_stats.html", urls = urls)

@shortener.errorhandler(404)
def page_not_found(e):
    return '<h1> 404 - Not Found</h1>', 404

