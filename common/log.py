#coding=utf-8
import os.path
import time, logging
import ctypes

FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01  # text color contains blue.
FOREGROUND_GREEN = 0x02  # text color contains green.
FOREGROUND_RED = 0x04  # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN
STD_OUTPUT_HANDLE = -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

class Log():
    def __init__(self, log_module):
        """
        log_module:为当前测试的模块名，一般是类名，比较好区分
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        :param logger:
        """
        #log_path = 'D:\GitHub\\at_jyb\logs\\'
        rq = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
        #log_path = os.path.dirname(os.getcwd()) + '\\logs\\'
        #self.log_name = log_path + rq + '.log'
        self.log_name = 'D:\GitHub\\at_jyb\logs\jyb.log'
     # 创建logger
        self.logger = logging.getLogger(log_module)
        self.logger.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')

    def __console(self, level, message):
        #创建一个fileHandler用于写日志到本地
        fh = logging.FileHandler(self.log_name, 'a+', encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

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
        fh.close()
        #return self.logger

    def debug(self, message, color=FOREGROUND_BLUE):
        set_color(color)
        self.__console('debug', message)
        set_color(FOREGROUND_WHITE)
        #return self.logger

    def warning(self, message, color= FOREGROUND_YELLOW):
        set_color(color)
        self.__console('warning', message)
        set_color(FOREGROUND_WHITE)
        #return self.logger

    def error(self, message, color=FOREGROUND_RED):
        set_color(color)
        self.__console('error', message)
        set_color(FOREGROUND_WHITE)
        #return self.logger

    def info(self, message, color=FOREGROUND_GREEN):
        set_color(color)
        self.__console('info', message)
        set_color(FOREGROUND_WHITE)
        #return self.logger

    # def getLog(self):
    #     return self.logger

if __name__ == '__main__':

    """
    log=Log("Test color")
    log.info("开始测试日志调试脚本")
    log.info("请输入日志调试等级")
    log.error("有错误啦！")
    log.warning("测试结束")
    """



