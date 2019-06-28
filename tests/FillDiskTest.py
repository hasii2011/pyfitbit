
from BaseTest import BaseTest

import logging
import os
import uuid
import shutil

class FillDisk(BaseTest):
    """"""

    @classmethod
    def setUpClass(cls):
        """"""
        BaseTest.setUpLogging()

    def setUp(self):
        """"""
        self.logger = logging.getLogger(__name__)

    def testWrite(self):
        ''''''

        sourceFilename      = "/Volumes/MyPassport/BigFile.mkv"
        destinationFilename = str(uuid.uuid4())
        destinationFilename = "/Volumes/MyPassport/" + destinationFilename + ".mkv"
        os.makedirs(os.path.dirname(destinationFilename), exist_ok=True)

        shutil.copy(sourceFilename, destinationFilename)
