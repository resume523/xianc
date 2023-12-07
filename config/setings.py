import os
import sys


class Config:
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    listpath=os.path.dirname(os.path.dirname(__file__))
    logreport=os.sep.join([listpath,"log"])
    realreport=os.sep.join([listpath,"report"])
    print(logreport)

if __name__ == '__main__':
    config=Config()
    print(config.logreport)
