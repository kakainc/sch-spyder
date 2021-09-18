# --->
# Created by liumeiyu on 2021/9/18.
# '_'

import logging


def log_init():
    log_path = '../logs.txt'
    logging.basicConfig(level=logging.DEBUG,
                        filename=log_path,                    # 指定日志输出目标文件的文件名
                        filemode='a',                         # 有w和a，w每次都会重新写日志，覆盖之前的日志
                        format="%(asctime)s %(name)s %(levelname)s %(message)s",
                        datefmt='%Y-%m-%d  %H:%M:%S %a'       # 指定时间格式
                        )
    logging.info("logging have ready !")
