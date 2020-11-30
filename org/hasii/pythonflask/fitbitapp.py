
import logging.config

from org.hasii.pythonflask.fitbit import app

logger = logging.getLogger(__name__)

secret_key = "The secret key is: " + app.config['SECRET_KEY']
logger.info("secret key: %s", secret_key)

if __name__ == "__main__":
    app.run()
