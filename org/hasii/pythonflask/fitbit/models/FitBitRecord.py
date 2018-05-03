
from org.hasii.pythonflask.fitbit import db

class FitBitRecord(db.Model):
    """"""

    id       = db.Column(db.Integer, primary_key=True)
    date     = db.Column(db.String(32))
    steps    = db.Column(db.Integer)
    calories = db.Column(db.Integer)

    def __repr__(self):
        return '<id: {} date: {}>'.format(self.id, self.date)
