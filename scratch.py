#!/usr/bin/python3
# encoding: utf-8
import requests
import http
import urllib, urllib3

url = "http://web.juhe.cn:8080/finance/exchange/rmbquot"


def get(url):
    print(url)
    res = requests.get(url)
    result = res.text
    print(result)


get(url)


# req = urllib3.HTTPResponse(url)
# print(req)
#
# res_data = urllib3.response(req)
# res = res_data.read()
# print(res)



currency_str_value = input("input currency value( exit when input Q ): ")

USD_VS_CNY = 6.77

while currency_str_value != "Q":
    unit = currency_str_value[-3:]
    currency_value = eval(currency_str_value[:-3])
    if unit == "USD":
        rmb_value = currency_value * USD_VS_CNY
        print("CNY is :", rmb_value)
    elif unit == "CNY":
        usd_value = currency_value / USD_VS_CNY
        print("USD is :", usd_value)
    else:
        print("not suppot!!")
    print("***********")
    currency_str_value = input("input currency value( exit when input Q ): ")

print("exit! thank you !")
