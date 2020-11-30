import logging

from tests.BaseTest import BaseTest

from org.hasii.pythonflask.fitbit import db
from org.hasii.pythonflask.fitbit.models.FitBitRecord import FitBitRecord


class DBTest(BaseTest):
    """"""
    @classmethod
    def setUpClass(cls):
        """"""
        BaseTest.setUpLogging()

    def setUp(self):
        """"""
        self.logger = logging.getLogger(__name__)

    def testDBWrite(self):
        """"""

        rec = FitBitRecord(date="2018-03-01", steps=777, calories=888)
        db.session.add(rec)
        db.session.commit()

        r = FitBitRecord.query.all()
        self.logger.info("%s", r)
