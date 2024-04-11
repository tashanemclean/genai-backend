import logging
import sys

logger = logging.getLogger()
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
streamHandler.setLevel(logging.INFO)
logger.setLevel(logging.INFO)
logger.addHandler(streamHandler)