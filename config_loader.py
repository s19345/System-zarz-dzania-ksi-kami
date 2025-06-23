import json

from logger import set_up_logger

logger = set_up_logger(__name__)

def load_config(file):
    """retrieves data from configuration file"""
    with open(file) as f:
        logger.info(f"Loading configuration from {file}")
        return json.load(f)
