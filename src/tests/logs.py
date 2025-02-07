import logging
import datetime

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger: logging.Logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.debug(datetime.datetime.now().isoformat())

    print("\n🐬")