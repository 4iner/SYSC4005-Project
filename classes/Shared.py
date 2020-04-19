import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.Logger("logger")
logFormatter = logging.Formatter("%(asctime)s : %(message)s")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logFormatter)


logger.addHandler(handler)

# Shared class that is used to make simulation easier and provides logging
class Shared:
    timeFactor = 100



    def timeFromString(st):
        return float(st)/Shared.timeFactor

    def log(txt):
        # logger.info(txt)
        pass;
