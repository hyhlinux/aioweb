# coding:utf-8
# 可以被所有模块导入

import logging
import datetime

# logging.basicConfig(
#   # filename='/tmp/apkpure_dcma.log',
#   level=logging.INFO,
#   format='%(asctime)s:%(funcName)15s:%(lineno)5s%(levelname)8s:%(name)10s:%(message)s',
#   datefmt='%Y/%m/%d %I:%M:%S' # )
# logging.basicConfig(level=logging.INFO)
log_format = '%(asctime)s:%(lineno)5s:%(name)10s:%(levelname)8s:%(message)s'
log_filename = '/tmp/test.log'


def create_log(name, level=logging.DEBUG, filename=log_filename, fhb=False, chb=True, format=log_format):
    new_log = logging.getLogger(name)
    new_log.setLevel(level)
    formatter = logging.Formatter(format)
    if fhb:
        fh = logging.FileHandler(filename)
        fh.setLevel(level)
        fh.setFormatter(formatter)
        new_log.addHandler(fh)

    if chb:
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        new_log.addHandler(ch)

    new_log.info('create ok!!')
    return new_log


def get_log(name=''):
    return create_log(name)


def main():
    log = get_log()
    log.info('log ok')

if __name__ == '__main__':
    main()
