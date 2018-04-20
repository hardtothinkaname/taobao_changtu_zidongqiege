# import numpy as np
# from matplotlib import pyplot as plt
from my_network import my_net as mnet
from business_re import taobao_re as tb_re, tianmao_re as tm_re
import re
import json


def download_pics(urls, prefix_name=""):
    temp1 = 1
    for my_url in urls:
        str1 = prefix_name + str(temp1)
        mnet.download_img(r"d:/downPics/", my_url, str1)
        print(str1 + "已下载！")
        temp1 += 1


def judge_url_type(url):
    #     判断url的类型，是天猫，淘宝，还是1688
    taobao_flag = re.search("item.taobao.com", url)
    if(taobao_flag):
        return "taobao"

    tianmao_flag = re.search(".tmall.com", url)
    if (tianmao_flag):
        return "tianmao"
    # print("")

if __name__ == '__main__':

    temp_str = r"111apiImgInfo  : '//tds.alicdn.com/json/item_imgs.htm?t=TB1cAiFiv5TBuNjSspmXXaDRVXa&sid=498203658&id=24181980727&s=f56a9247beacb582a03a0c6661d6a8bc&v=2&m=1',"
    temp_str2 = r'!498203658.jpg":{"w":750, "h":1060},"TB2FYiltVXXXXaKXXXXXXXXXXXX-498203658.jpg":{"w":750, "h":844},"TB2aWR0sYFlpuFjy0FgXXbRBVXa_!!498203658.jpg":{"w":'
    temp_str3 = r"https://item.taobao.com/item.htm?spm=a230r.1.14.27.379948f9AbDeiT&id=41119941557&ns=1&abbucket=16#detail"

    url = "https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-16801072333.25.610e793dECOm2Q&id=43649469372"
    url = "https://item.taobao.com/item.htm?spm=a230r.1.14.48.131e6ab3LJeKpP&id=529747601133&ns=1&abbucket=14#detail"
    # url = "https://detail.1688.com/offer/561345651056.html?spm=a261y.7663282.0.0.d59b588aI9fP4t"

    # 天猫店，测试
    # url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.13.131e6ab3LJeKpP&id=42834094508&cm_id=140105335569ed55e27b&abbucket=14"

    zhu_tu_urls = []
    fen_lei_pic_urls = []
    detail_img_urls = []

    html = ""
    re_module = ""
    if judge_url_type(url) == "tianmao":
        html = mnet.get_html2(url)
        re_module = tm_re

    if judge_url_type(url) == "taobao":
        html = mnet.get_html(url)
        re_module = tb_re


    # zhu_tu_urls = re_module.get_zhutu_urls_from_string(html)
    # fen_lei_pic_urls = re_module.get_fen_lei_urls_from_string(html)
    # img_info_url = re_module.get_img_info_url_from_html(html)
    # sid = re_module.get_sid_from_img_info_url(img_info_url)
    # detail_img_info_json = mnet.get_html(img_info_url)
    # detail_img_urls = re_module.get_all_detail_pic_url_from_json(detail_img_info_json, sid)



    #
    # download_pics(zhu_tu_urls, '1主图')
    # download_pics(fen_lei_pic_urls, '2颜色分类')
    # download_pics(detail_img_urls, '3详情图')

    price_url = re_module.get_price_url_from_html(html)
    price_json = mnet.get_html_with_referer(price_url, referer=url)
    json1 = json.loads(price_json)
    pattern = r'<li data-value=.*?<span>(.*?)</span>'
    return_str = re.findall(pattern, html, re.S)

    print("successed!")