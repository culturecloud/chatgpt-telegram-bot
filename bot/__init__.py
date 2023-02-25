from os import path
import logging
from bot.log_config import setup_logging

if path.exists('info.log'):
    with open('info.log', 'r+') as f:
        f.truncate(0)
if path.exists('debug.log'):
    with open('debug.log', 'r+') as f:
        f.truncate(0)

setup_logging()
logger = logging.getLogger(__name__)