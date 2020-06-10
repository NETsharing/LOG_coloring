logging.addLevelName(logging.DEBUG, "\033[1;34m{}\033[1;0m".format(logging.getLevelName(logging.DEBUG)))
logging.addLevelName(logging.INFO, "\033[1;32m{}\033[1;0m".format(logging.getLevelName(logging.INFO)))
logging.addLevelName(logging.WARNING, "\033[1;33m{}\033[1;0m".format(logging.getLevelName(logging.WARNING)))
logging.addLevelName(logging.ERROR, "\033[1;31m{}\033[1;0m".format(logging.getLevelName(logging.ERROR)))
logging.addLevelName(logging.CRITICAL, "\033[1;41m{}\033[1;0m".format(logging.getLevelName(logging.CRITICAL)))

LOG_LEVEL = config['logging']['log_level']
LOG_PATH = config['logging']['log_path']
FORMATTER = logging.Formatter(config['logging']['log_format'])

stream_handler = logging.StreamHandler()
stream_handler.setLevel(LOG_LEVEL)
stream_handler.setFormatter(FORMATTER)
logger = logging.getLogger()
logger.addHandler(stream_handler)

file_handler = logging.FileHandler(LOG_PATH)
file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(FORMATTER)
