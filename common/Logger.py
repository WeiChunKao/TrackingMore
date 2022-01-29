# -*- coding: utf-8 -*-
import logging
import os
from logging import handlers


def mkdirLogFolder():
    """[summary]
       當前路徑建立LOG資料夾
    """
    if not os.path.exists('log'):
        os.mkdir('log')


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日誌級別關係對映

    def __init__(self, filename, level='info', when='D', backCount=1, fmt='%(asctime)s -[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 設定日誌格式
        self.logger.setLevel(self.level_relations.get(level))  # 設定日誌級別
        sh = logging.StreamHandler()  # 往螢幕上輸出
        sh.setFormatter(format_str)  # 設定螢幕上顯示的格式
        th = handlers.TimedRotatingFileHandler(
            filename=filename, when=when, backupCount=backCount, encoding='utf-8')  # 往檔案裡寫入#指定間隔時間自動生成檔案的處理器
        # 例項化TimedRotatingFileHandler
        # interval是時間間隔，backupCount是備份檔案的個數，如果超過這個個數，就會自動刪除，when是間隔的時間單位，單位有以下幾種：
        # S 秒
        # M 分
        # H 小時、
        # D 天、
        # W 每星期（interval==0時代表星期一）
        # midnight 每天凌晨
        # 如果已經存在則清掉，重新加一個
        if (self.logger.hasHandlers()):
            self.logger.handlers.clear()
        th.setFormatter(format_str)  # 設定檔案裡寫入的格式
        self.logger.addHandler(sh)  # 把物件加到logger裡
        self.logger.addHandler(th)


if __name__ == '__main__':
    mkdirLogFolder()
    log = Logger('test.log', level='debug')
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning('警告')
    log.logger.error('報錯')
    log.logger.critical('嚴重')
    Logger('error.log', level='error').logger.error('error')
    # os.system("pause")
else:
    mkdirLogFolder()
