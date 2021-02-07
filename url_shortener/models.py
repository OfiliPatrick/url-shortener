from .extensions import db
from datetime import datetime

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(3), unique=True)
    views = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default=datetime.now)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        new_url = "2p1q"
        url_exist = self.query.filter_by(short_url=new_url).first()
        
        if url_exist:
           return self.generate_short_url()

        return new_url


