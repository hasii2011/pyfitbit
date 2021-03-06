
import os
import logging
import logging.config

from unittest import TestCase


class BaseTest(TestCase):
    """"""

    @classmethod
    def setUpLogging(cls):
        """"""
        cls.findLoggingConfig()
        logging.config.fileConfig('logging.conf')

    @classmethod
    def findLoggingConfig(cls):
        """"""
        if os.path.isfile("logging.conf"):
            return
        else:
            os.chdir("../")
            cls.findLoggingConfig()
