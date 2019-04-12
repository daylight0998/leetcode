# -*- coding:utf8 -*-
# !/usr/bin/python


import re
import time

import urllib
import urllib.request
import urllib.parse

# import itchat


class CoraCMB:
    """China Merchants Bank."""

    def __init__(self):
        super(CoraCMB, self).__init__()
        self._items = []
        self._html = self._message = ''

    def _loadurl(self):
        """Loading  抓取招商银行 http://english.cmbchina.com/Rate/ForexRates.aspx 网页地址的汇率内容，分离出 U.S. Dollar 汇率 """
        url = 'http://english.cmbchina.com/Rate/ForexRates.aspx'
        try:
            response = urllib.request.urlopen(url)
            self._html = response.read().decode('UTF-8')
        except BaseException:
            return False
        return True

    def lastrates(self, currency=['U.S. Dollar']):
        """Latest FX exchange rates， 如果拉取页面失败返回空"""
        if self._loadurl() is False:
            return ''
        self._message = ''
        currency_rate = 0
        """ 获取匹配到的页面 表格行标签 <tr.*?>(.*?)</tr> 的数据 """
        itmegroup = re.findall(r'<tr.*?>(.*?)</tr>', self._html, re.S | re.M)
        for items in itmegroup:
            """ 首先替换空格，转行等无用信息为空，然后获取匹配到的表格行标签里的每列元素 <td.*?>(.*?)</td> 的数据 放到 item 数组里面"""
            self._items = [i.replace('\r\n', '').strip(' ') for i in
                           re.findall(r'<td.*?>(.*?)</td>', items, re.S | re.M)]
            # print(self._items)
            """ 对第一列元素数据判断 如果是 U.S. Dollar 则输出对应汇率人民币出售汇率 self._items[4] """
            if self._items[0] in currency:
                self._message += '{0} (SO)={1} (SI)={2} '.format(self._items[0], self._items[4], self._items[5])
                currency_rate = self._items[4]

        print(currency_rate)
        # return self._message
        return currency_rate


def main():
    currency_str_value = input("input currency value( exit when input Q ): ")

    while currency_str_value != "Q":
        cmb = CoraCMB()
        USD_VS_CNY = round(float(cmb.lastrates()) / 100, 2)
        print(USD_VS_CNY)
        # USD_VS_CNY = 6.77 # 用上面2行完成汇率抓取。cmb.lastrates() 拿到 每100美元所输出的汇率，然后转化为 float 类型 除以100，精确到后2位 的汇率。

        unit = currency_str_value[-3:]
        currency_value = eval(currency_str_value[:-3])
        if unit == "USD":
            rmb_value = round(currency_value * USD_VS_CNY, 2)
            print("CNY is :", rmb_value)
        elif unit == "CNY":
            usd_value = round(currency_value / USD_VS_CNY, 2)
            print("USD is :", usd_value)
        else:
            print("not suppot!!")
        print("***********")
        currency_str_value = input("input currency value( exit when input Q ): ")

    print("exit! thank you !")


    # itchat.auto_login(enableCmdQR=2, hotReload=True)

    # while True:
    #     hours = time.localtime(time.time()).tm_hour
    #     if hours > 21 or hours < 9:
    #         time.sleep(60 * 10)
    #         continue
    #
    #     # itchat.send(cmb.lastrates(), toUserName='filehelper')
    #     print(cmb.lastrates())
    #     time.sleep(60 * 10)

print(__name__)
if __name__ == '__main__':
    main()
