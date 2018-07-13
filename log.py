import logging

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger(name="Learning")


logger.info("Information will be logged", extra=d)
logger.debug("debug will be logged", extra=d)
logger.error("error will be logged", extra=d)
logger.log("log will be logged", extra=d)

