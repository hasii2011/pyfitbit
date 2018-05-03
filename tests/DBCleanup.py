
from org.hasii.pythonflask.fitbit import db
from org.hasii.pythonflask.fitbit.models.FitBitRecord import FitBitRecord

recs = FitBitRecord.query.all()
for r in recs:
    print("Delete " + r.__repr__())
    db.session.delete(r)

db.session.commit()