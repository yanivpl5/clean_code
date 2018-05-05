import logging

#FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
#logging.basicConfig(filename="/Users/yaniv/clean_code.log", level=logging.INFO, format=FORMAT)
#logging.basicConfig(format=FORMAT)
#formatter = logging.Formatter('%(levelname)-8s : %(message)s')
logger = logging.getLogger("logging1")
logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler("/Users/yaniv/clean_code.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)



try:
    filePath = "/var/log/somelog.log"
    open(filePath)
except FileNotFoundError:
    logger.error("Failed to open file from path", filePath)
