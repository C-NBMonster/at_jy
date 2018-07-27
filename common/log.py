#coding=utf-8
import os
import time,logging

#log_path = os.path.dirname(os.getcwd()) + '\AT_Demo_Show\logs\\'
log_path = '\Py_Projects\AT_Demo_Show\logs\\'

class Log():
    def __init__(self,log_module):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        :param logger:
        """
        rq = time.strftime('%Y%m%d %H%M%S', time.localtime(time.time()))
        self.log_name = log_path + rq + '.log'

        # 创建一个logger
        self.logger = logging.getLogger(log_module)
        self.logger.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def __console(self,level,message):
        #创建一个fileHandler用于写日志到本地
        fh=logging.FileHandler(self.log_name,'a+')
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #设置输出格式
        fh.setFormatter(self.formatter)
        ch.setFormatter(self.formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        #避免日志重复输出
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

    def debug(self,message):
         self.__console('debug',message)
    def warning(self,message):
         self.__console('warning',message)
    def error(self,message):
         self.__console('error',message)
    def info(self,message):
         self.__console('info',message)

if __name__ == '__main__':
    """
    log=Log()
    log.info("开始测试日志调试脚本")
    log.info("请输入日志调试等级")
    log.error("有错误啦！")
    log.warning("测试结束")
    """

