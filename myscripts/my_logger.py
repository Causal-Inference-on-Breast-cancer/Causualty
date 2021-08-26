import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename='../log/causal.log',
                    level=logging.DEBUG,
                    format= LOG_FORMAT)

logger = logging.getLogger()
