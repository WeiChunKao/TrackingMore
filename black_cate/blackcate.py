from common.BaseType import baseType, http
from typing import Tuple
import sys
import requests
import json


class Cat():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        "初始化logger物件"
        self.logger = baseType(self.__class__.__name__)

    def getLogin(self, trackingmore_api_key: str, url: str = 'https://api.trackingmore.com') -> Tuple[int, dict, dict]:
        """[summary]
        黑貓認證
        Args:
            trackingmore_api_key (str): "帳號的token"
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com'.

        Returns:
            dict: 認證資訊
        """
        try:
            response = requests.get(
                url, headers=http.Header(trackingmore_api_key))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('GET')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('GET')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('GET')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('GET')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('GET')

    def getCarriers(self, trackingmore_api_key: str, lang: str = 'en', url: str = 'https://api.trackingmore.com/v2/carriers/') -> Tuple[int, dict, dict]:
        """[summary]
        取得貨物資訊
        Args:
            trackingmore_api_key (str): 帳號的token
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/carriers/'.

        Returns:
            Tuple[int, dict, dict]: 快遞清單
        """
        try:
            response = requests.get(
                url, headers=http.carriersHeader(trackingmore_api_key, lang))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('GET')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('GET')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('GET')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('GET')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('GET')

    def getDetectCourier(self, trackingmore_api_key: str, tracking_number: str, url: str = 'https://api.trackingmore.com/v2/carriers/detect') -> Tuple[int, dict, dict]:
        """[summary]
        取得檢查包裹快遞
        Args:
            trackingmore_api_key (str): 帳號的token
            tracking_number (str): 包裹號碼
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/carriers/detect'.

        Returns:
            Tuple[int, dict, dict]: 包裹資訊
        """
        try:
            response = requests.post(
                url, data={'tracking_number': tracking_number}, headers=http.Header(trackingmore_api_key, 'POST'))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('POST')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('POST')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('POST')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('POST')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('POST')

    def getCreateTracking(self, trackingmore_api_key: str, tracking_number: str, carrier_code: str, url: str = 'https://api.trackingmore.com/v2/trackings/post') -> Tuple[int, dict, dict]:
        """[summary]
        建立追蹤
        Args:
            trackingmore_api_key (str): 帳號的token
            tracking_number (str): 貨物編號
            carrier_code (str): 送貨模式
            url (str, optional): [description]. Defaults to https://api.trackingmore.com/v2/trackings/post'.

        Returns:
            dict: 建立追蹤資訊
        """
        try:
            response = requests.post(
                url, data={"tracking_number": tracking_number, "carrier_code": carrier_code}, headers=http.Header(trackingmore_api_key, 'POST'))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('POST')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('POST')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('POST')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('POST')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('POST')

    def getResultTracking(self, trackingmore_api_key: str, carrier_code: str, tracking_number: str, lang: str = 'en', url: str = 'https://api.trackingmore.com/v2/trackings/') -> Tuple[int, dict, dict]:
        f"""[summary]
        黑貓認證
        Args:
            trackingmore_api_key (str): 帳號的token
            carrier_code (str): 運輸模式
            tracking_number (str): 追蹤編號
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/trackings/{carrier_code}/{tracking_number}/{lang}'.

        Returns:
            dict: 追蹤結果資訊
        """
        try:
            response = requests.get(
                f"{url}{carrier_code}/{tracking_number}/{lang}", headers=http.Header(trackingmore_api_key))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('GET')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('GET')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('GET')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('GET')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('GET')

    def getModifyTracking(self, trackingmore_api_key: str, carrier_code: str, tracking_number: str, logistics_channel: str, customer_email: str, order_id: str, url: str = 'https://api.trackingmore.com/v2/trackings/') -> Tuple[int, dict, dict]:
        f"""[summary]
        修改追蹤
        Args:
            trackingmore_api_key (str): 帳號的token
            carrier_code (str): 運送模式
            tracking_number (str): 追蹤編號
            logistics_channel (str): [description]
            customer_email (str): 信箱
            order_id (str): 訂單
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/trackings/{carrier_code}/{tracking_number}'.

        Returns:
            Tuple[int, dict, dict]: 修改結果
        """
        try:
            response = requests.put(
                f"{url}{carrier_code}/{tracking_number}", data={
                    'logistics_channel': logistics_channel,
                    'customer_email': customer_email,
                    'order_id': order_id
                }, headers=http.Header(trackingmore_api_key, 'PUT'))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('PUT')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('PUT')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('PUT')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('PUT')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('PUT')

    def getDeleteTracking(self, trackingmore_api_key: str, carrier_code: str, tracking_number: str, url: str = 'https://api.trackingmore.com/v2/trackings/') -> Tuple[int, dict, dict]:
        f"""[summary]
        刪除追蹤資訊
        Args:
            trackingmore_api_key (str): 帳號的token
            carrier_code (str): 運送模式
            tracking_number (str): 追蹤編號
            url (str, optional): [description]. Defaults to f'https://api.trackingmore.com/v2/trackings/{carrier_code}/{tracking_number}'.

        Returns:
            Tuple[int, dict, dict]: 刪除追蹤資訊
        """
        try:
            response = requests.delete(
                f"{url}{carrier_code}/{tracking_number}", headers=http.Header(trackingmore_api_key, 'DELETE'))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('DELETE')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('DELETE')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('DELETE')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('DELETE')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('DELETE')

    def getMultiCreateTracking(self, trackingmore_api_key: str, param: list, url: str = 'https://api.trackingmore.com/v2/trackings/batch') -> Tuple[int, dict, dict]:
        """[summary]
        建立多筆追蹤
        Args:
            trackingmore_api_key (str): 帳號的token
            param (list): 多筆清單陣列
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/trackings/batch'.

        Returns:
            Tuple[int, dict, dict]: 多筆追蹤資訊
        """
        try:
            response = requests.post(
                url, data=param, headers=http.Header(trackingmore_api_key, 'POST'))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('POST')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('POST')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('POST')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('POST')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('POST')

    def getMultiResultsTracking(self, trackingmore_api_key: str, numbers: str, url='https://api.trackingmore.com/v2/trackings/get') -> Tuple[int, dict, dict]:
        try:
            response = requests.get(
                url, params={'numbers': numbers}, headers=http.Header(trackingmore_api_key))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('GET')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('GET')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('GET')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('GET')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('GET')

    def getMultiDeleteTracking(self, trackingmore_api_key: str, params: list, url='https://api.trackingmore.com/v2/trackings/delete') -> Tuple[int, dict, dict]:
        """[summary]
        刪除多筆追蹤
        Args:
            trackingmore_api_key (str): 帳號的token
            params (list): 多筆追蹤清單
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/trackings/delete'.

        Returns:
            Tuple[int, dict, dict]: 刪除多筆追蹤結果
        """
        try:
            response = requests.post(
                url, data=params, headers=http.Header(trackingmore_api_key, 'POST'))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('POST')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('POST')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('POST')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('POST')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('POST')

    def getAccountInfo(self, trackingmore_api_key: str, url: str = 'https://api.trackingmore.com/v2/trackings/getuserinfo') -> Tuple[int, dict, dict]:
        """[summary]
        取得使用者資訊
        Args:
            trackingmore_api_key (str): 帳號的token
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/trackings/getuserinfo'.

        Returns:
            Tuple[int, dict, dict]: 使用者資訊
        """
        try:
            response = requests.get(
                url, headers=http.Header(trackingmore_api_key))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('GET')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('GET')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('GET')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('GET')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('GET')

    def getRealTimeResult(self, trackingmore_api_key: str, tracking_number: str, carrier_code: str, url: str = 'https://api.trackingmore.com/v2/trackings/realtime') -> Tuple[int, dict, dict]:
        """[summary]
        取得即時結果
        Args:
            trackingmore_api_key (str): 帳號的token
            tracking_number (str): 追蹤編號
            carrier_code (str): 運送模式
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/trackings/realtime'.

        Returns:
            Tuple[int, dict, dict]: 取得即時資訊
        """
        try:
            response = requests.post(
                url, data={"tracking_number": tracking_number, "carrier_code": carrier_code}, headers=http.Header(trackingmore_api_key, 'POST'))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('POST')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('POST')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('POST')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('POST')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('POST')

    def getChangeCourier(self, trackingmore_api_key: str, tracking_number: str, carrier_code: str, update_carrier_code: str, url: str = 'https://api.trackingmore.com/v2/trackings/update') -> Tuple[int, dict, dict]:
        """[summary]

        Args:
            trackingmore_api_key (str): 帳號的token
            tracking_number (str): 追蹤編號
            carrier_code (str): 目前運送方式
            update_carrier_code (str): 想更換的運送方式
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/trackings/update'.

        Returns:
            Tuple[int, dict, dict]: [description]
        """
        try:
            response = requests.post(
                url, data={
                    "tracking_number": tracking_number,
                    "carrier_code": carrier_code,
                    'update_carrier_code': update_carrier_code}, headers=http.Header(trackingmore_api_key, 'POST'))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('POST')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('POST')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('POST')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('POST')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('POST')

    def getStatusStatistics(self, trackingmore_api_key: str, created_at_min: str, created_at_max: str, url: str = 'https://api.trackingmore.com/v2/trackings/getstatusnumber') -> Tuple[int, dict, dict]:
        """[summary]
        取得貨物狀態
        Args:
            trackingmore_api_key (str): 帳號token
            created_at_min (str): 建立訂單時間(轉成分鐘)
            created_at_max (str): 結束時間(轉成分鐘)
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/trackings/getstatusnumber'.

        Returns:
            Tuple[int, dict, dict]: [description]
        """
        try:
            response = requests.get(
                url, params={'created_at_min': created_at_min, 'created_at_max': created_at_max}, headers=http.Header(trackingmore_api_key))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('GET')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('GET')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('GET')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('GET')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('GET')

    def getStopUpdatingTracking(self, trackingmore_api_key: str, params: list, url: str = 'https://api.trackingmore.com/v2/trackings/notupdate') -> Tuple[int, dict, dict]:
        """[summary]
        停止更新追蹤
        Args:
            trackingmore_api_key (str): 帳號的token
            params (list): [
                                {
                                    "tracking_number": "RU123456789CN",
                                    "carrier_code": "china-post"
                                },
                                {
                                    "tracking_number": "LX123456789CN",
                                    "carrier_code": "china-ems"
                                }
                            ]
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/trackings/notupdate'.

        Returns:
            Tuple[int, dict, dict]: 資訊
        """
        try:
            response = requests.post(
                url, data=params, headers=http.Header(trackingmore_api_key, 'POST'))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('POST')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('POST')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('POST')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('POST')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('POST')

    def getCheckRemoteArea(self, trackingmore_api_key: str, params: list, url: str = 'https://api.trackingmore.com/v2/trackings/remote') -> Tuple[int, dict, dict]:
        """[summary]
        檢查貨物是否發送偏遠地區
        Args:
            trackingmore_api_key (str): [description]
            params (list): [
                                {
                                    "country": "Japan",
                                    "postcode": "7621094"
                                },
                                {
                                    "country": "NZ",
                                    "postcode": "Papaaroha"
                                }
                            ]
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/trackings/remote'.

        Returns:
            Tuple[int, dict, dict]: 檢查資訊
        """
        try:
            response = requests.post(
                url, data=params, headers=http.Header(trackingmore_api_key, 'POST'))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('POST')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('POST')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('POST')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('POST')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('POST')

    def getTransitTime(self, trackingmore_api_key: str, params: list, url: str = 'https://api.trackingmore.com/v2/trackings/costtime') -> Tuple[int, dict, dict]:
        """[summary]
        取得中轉站時間
        Args:
            trackingmore_api_key (str): 帳號的token
            params (list): [
                                {
                                    "carrier_code": "dhl",
                                    "original": "CN",
                                    "destination": "US"
                                },
                                {
                                    "carrier_code": "dhl",
                                    "original": "CN",
                                    "destination": "RU"
                                }
                            ]
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/trackings/costtime'.

        Returns:
            Tuple[int, dict, dict]: 中轉站時間
        """
        try:
            response = requests.post(
                url, data=params, headers=http.Header(trackingmore_api_key, 'POST'))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('POST')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('POST')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('POST')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('POST')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('POST')

    def getTrackAirWaybill(self, trackingmore_api_key: str, track_number: str, url: str = 'https://api.trackingmore.com/v2/trackings/aircargo') -> Tuple[int, dict, dict]:
        """[summary]
        獲取空運清單
        Args:
            trackingmore_api_key (str): 帳號的token
            track_number (str): 追蹤號碼
            url (str, optional): [description]. Defaults to 'https://api.trackingmore.com/v2/trackings/aircargo'.

        Returns:
            Tuple[int, dict, dict]: [description]
        """
        try:
            response = requests.post(
                url, data={'track_number': track_number}, headers=http.Header(trackingmore_api_key, 'POST'))
            response.close()
            self.logger.writeLog(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{response.status_code}，{json.loads(response.text)}")
            return json.loads(response.text), response.status_code, http.apiHeaders('POST')
        except requests.exceptions.Timeout as timeout:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{timeout}")
            return http.apiResponse(408, "Request Timeout", f"{timeout}"), 408,  http.apiHeaders('POST')
        except requests.exceptions.TooManyRedirects as tooManyRedirects:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{tooManyRedirects}")
            return http.apiResponse(11215, "Too Many Redirects", f"{tooManyRedirects}"), 11215,  http.apiHeaders('POST')
        except requests.exceptions.RequestException as requestException:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{requestException}")
            return http.apiResponse(400, "RequestException", f"{requestException}"), 400,  http.apiHeaders('POST')
        except Exception as e:
            self.logger.writeError(
                f"{sys._getframe().f_code.co_name}=>{trackingmore_api_key}-->{e}")
            return http.apiResponse(400, "Exception", f"{e}"), 400,  http.apiHeaders('POST')
