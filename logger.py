import logging

logging.basicConfig(
            filename="compiler.log",
            format='%(asctime)s %(levelname)s %(message)s', 
            level=logging.INFO, 
            datefmt='%m/%d/%Y %I:%M:%S %p'
            )
logger = logging.getLogger("waitress")