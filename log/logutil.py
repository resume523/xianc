import logging
import os.path
import time
from xianc.config.setings import Config

Stream=True
config=Config()
tt=config.logreport
class LogUtil:
    def __init__(self):
        self.logger=logging.getLogger("logger")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            self.log_name='{}.log'.format(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime()))
            self.log_path_file=os.path.join(tt,self.log_name)
            fh=logging.FileHandler(self.log_path_file,encoding='utf-8',mode='w')
            fh.setLevel(logging.INFO)
            formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
            fh.close()
            if Stream:
                fh_stream=logging.StreamHandler()
                fh_stream.setLevel(logging.INFO)
                fh_stream.setFormatter(formatter)
                self.logger.addHandler(fh_stream)
    def log(self):
        return self.logger
logger=LogUtil().log()
if __name__ == '__main__':
    logger.info('test')