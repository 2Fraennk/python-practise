import logging
from properties import Props

logger = logging.getLogger(__name__)
filename = f"./../{Props.LOG_PATH}/{Props.LOG_FILE}"
logger = logging.getLogger(__name__)
logging.basicConfig(level='DEBUG', filename=filename, filemode='a',
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')