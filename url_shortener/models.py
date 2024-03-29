"""A module containing app entities"""

from datetime import datetime
from .extensions import db
from .utils import base62_encoding

class Url(db.Model):
    """Blueprint for Url entity"""
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(8), unique=True)
    views = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        """Assigns short_url field to generated short url upon object creation"""
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        """ Generates and returns Slug  """
        new_url = base62_encoding(8)
        url_exist = self.query.filter_by(short_url=new_url).first()
        if url_exist:
            return self.generate_short_url()

        return new_url
