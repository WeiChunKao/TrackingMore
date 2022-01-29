# -*- coding: utf-8 -*-
from common.Logger import Logger


class http:
    @staticmethod
    def Header(Trackingmore_Api_Key: str, type: str = 'GET') -> dict:
        """[summary]
        取得黑貓 api的header
        Args:
            Trackingmore_Api_Key (str): 帳號的API TOKEN

        Returns:
            [dict]: 回傳login header
        """
        return {
            "Content-Type": "application/json",
            "Trackingmore-Api-Key": f"{Trackingmore_Api_Key}",
            'Connection': 'close',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': f'{type}',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }

    @staticmethod
    def carriersHeader(Trackingmore_Api_Key: str, Lang: str) -> dict:
        """[summary]
        取得黑貓貨物資訊api的Header
        Args:
            Trackingmore_Api_Key (str): 帳號的token
            Lang (str, optional): 語系 Defaults to 'en'.

        Returns:
            dict: Header
        """
        return {
            "Content-Type": "application/json",
            "Trackingmore-Api-Key": f"{Trackingmore_Api_Key}",
            'Connection': 'close',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type',
            "Lang": f"{Lang}"
        }

    @staticmethod
    def apiResponse(statusCode: int, type: str, message: str) -> dict:
        """[summary]
        讓api回傳與黑貓相同格式
        Args:
            statusCode (int): 狀態碼
            type (str): 型別
            message (str): 訊息

        Returns:
            dict: 與黑貓格式相同
        """
        return {
            "meta": {
                "code": statusCode,
                "type": f"{type}",
                "message": f"{message}",
            },
            "data": []
        }

    @staticmethod
    def apiHeaders(type: str) -> dict:
        """[summary]
        api回傳headers
        Args:
            type (str): GET、POST..etc

        Returns:
            dict: Headers
        """
        return {
            "Content-Type": "application/json",
            'Connection': 'close',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': f'{type}',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }


class baseType:
    def __init__(self, filename: str = None):
        """[summary]
           初始化Logger物件
        Args:
            filename ([string], optional): 如果是繼承此物件，filename為NONE反之傳入檔名 Defaults to None.
        """
        if not filename:
            self.__log = Logger(
                './log/' + self.__class__.__name__ + '.log', level='debug')
        else:
            self.__log = Logger(
                './log/' + filename + '.log', level='debug')

    def writeLog(self, text: str):
        """[summary]
            Write Info
        Args:
            text ([string]): messages
        """
        self.__log.logger.info(text)

    def writeError(self, text: str):
        """[summary]
            Write Error
        Args:
            text ([string]): messages
        """
        self.__log.logger.error(text)

    def writeWarning(self, text: str):
        """[summary]
            Write Warning
        Args:
            text ([string]): messages
        """
        self.__log.logger.warning(text)

    def writeDebug(self, text: str):
        """[summary]
            Write Debug
        Args:
            text ([string]): messages
        """
        self.__log.logger.debug(text)

    def writeCritical(self, text: str):
        """[summary]
            Write Critical
        Args:
            text ([string]): messages
        """
        self.__log.logger.critical(text)
