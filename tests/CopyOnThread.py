"""
Copying a file and checking its progress while it's copying.
"""

import os
import shutil
import threading
import time
import uuid
import logging
import logging.config

def setUpLogging():
    """"""
    findLoggingConfig()
    logging.config.fileConfig('logging.conf')

def findLoggingConfig():
    """"""
    if os.path.isfile("logging.conf"):
        return
    else:
        os.chdir("../")
        findLoggingConfig()

def checker(source_path, destination_path):
    """
    Compare 2 files till they're the same and print the progress.

    :type source_path: str
    :param source_path: path to the source file
    :type destination_path: str
    :param destination_path: path to the destination file
    """

    # Making sure the destination path exists
    while not os.path.exists(destination_path):
        logger.info("destination file '%s' does not yet exist", des)
        time.sleep(.99)

    # Keep checking the file size till it's the same as source file
    while os.path.getsize(source_path) != os.path.getsize(destination_path):
        logger.info("%s%% complete",
                    int((float(os.path.getsize(destination_path))/float(os.path.getsize(source_path))) * 100))
        time.sleep(30.00)

    logger.info("Checking thread is done")


def copying_file(source_path, destination_path):
    """
    Copying a file

    :type source_path: str
    :param source_path: path to the file that needs to be copied
    :type destination_path: str
    :param destination_path: path to where the file is going to be copied
    :rtype: bool
    :return: True if the file copied successfully, False otherwise
    """
    logger.info("Copying....")
    shutil.copyfile(source_path, destination_path)

    if os.path.exists(destination_path):
        logger.info("Copying is done....")
        return True

    logger.info("Filed...")
    return False

#des = r'<PATH/TO/SPURCE/FILE>'
#src = r'<PATH/TO/DESTINATION/FILE>'

setUpLogging()
logger = logging.getLogger(__name__)

src       = "/Volumes/MyPassport/BigFile.mkv"
iteration = 0
while iteration < 20:

    des     = "/Volumes/MyPassport/" + str(uuid.uuid4())
    threads = []

    logger.info("Big file copy name: %s", des)

    t = threading.Thread(group=None, name='copying', target=copying_file, args=(src, des))
    # Start the copying on a separate thread
    t.start()
    # Checking the status of destination file on a separate thread
    b = threading.Thread(group=None, name='checking', target=checker, args=(src, des))
    b.start()

    threads.append(t)
    threads.append(b)

    # Wait for all threads to complete
    for t in threads:
       t.join()

    logger.info("Finished iteration %s", iteration)
    iteration = iteration + 1
    threads.clear()

logger.info ("Exiting Main Thread")