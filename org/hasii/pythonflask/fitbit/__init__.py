import os

import logging.config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from org.hasii.pythonflask.fitbit.Configuration import Configuration
#
#
#
logConfigDir = os.getenv("LOG_CONFIG_PATH")
if logConfigDir is None:
    raise AssertionError("LOG_CONFIG_PATH not set")

logging.config.fileConfig(logConfigDir + '/logging.conf')

logger = logging.getLogger(__name__)

logger.info("Module name: %s", __name__)

app = Flask(__name__)

app.config["DEBUG"] = True
app.config.from_object(Configuration)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
#
# Avoid circular imports
#
from org.hasii.pythonflask.fitbit import routes
from org.hasii.pythonflask.fitbit.models import FitBitRecord
