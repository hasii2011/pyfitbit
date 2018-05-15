import os
import logging
import csv

from BaseTest import BaseTest

from org.hasii.pythonflask.fitbit import db
from org.hasii.pythonflask.fitbit.models.FitBitRecord import FitBitRecord

class DBLoader(BaseTest):
    """"""
    DEFAULT_DATA_DIRECTORY = "FitBit_Data"
    FILE_PREFIX            = "fitbit_export_"

    baseDirectory          = None
    dataDirectory          = None

    @classmethod
    def setUpClass(cls):
        """"""
        BaseTest.setUpLogging()

    def setUp(self):
        """"""
        self.logger = logging.getLogger(__name__)
        self.baseDirectory = os.getcwd()
        self.dataDirectory = self.baseDirectory + "/" + DBLoader.DEFAULT_DATA_DIRECTORY + "/"


    def testLoadDB(self):
        """"""

        recCount = 0
        for root, directories, fileNames in os.walk(self.dataDirectory):

            for fileName in fileNames:

                filePath = os.path.join(root, fileName)
                self.logger.info("datafile: %s", filePath)

                csvfile = open(filePath, "r")

                fitBitDictReader = csv.DictReader(csvfile)
                self.logger.info("fieldnames: %s", fitBitDictReader.fieldnames)

                for row in fitBitDictReader:

                    self.logger.info("Date: %s  Steps: %s  Calories Burned %s", row['Date'], row['Steps'], row['Calories Burned'])
                    rec = FitBitRecord(date=row['Date'], steps=row['Steps'], calories=row['Calories Burned'])
                    db.session.add(rec)
                    recCount +=1

                db.session.commit()
                csvfile.close()

            self.logger.info("Loaded %s records", recCount)

if __name__ == '__main__':
    unittest.main()
