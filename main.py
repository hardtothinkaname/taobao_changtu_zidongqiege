# import numpy as np
# from matplotlib import pyplot as plt
import urllib3
import re
from my_network import my_net as mnet
import tao_bao_re as tb_re


def download_pics(urls, prefix_name=""):
    temp1 = 1
    for my_url in urls:
        str1 = prefix_name + str(temp1)
        mnet.download_img(r"d:/downPics/", my_url, str1)
        print(str1 + "已下载！")
        temp1 += 1


if __name__ == '__main__':

    temp_str = r"111apiImgInfo  : '//tds.alicdn.com/json/item_imgs.htm?t=TB1cAiFiv5TBuNjSspmXXaDRVXa&sid=498203658&id=24181980727&s=f56a9247beacb582a03a0c6661d6a8bc&v=2&m=1',"
    temp_str2 = r'!498203658.jpg":{"w":750, "h":1060},"TB2FYiltVXXXXaKXXXXXXXXXXXX-498203658.jpg":{"w":750, "h":844},"TB2aWR0sYFlpuFjy0FgXXbRBVXa_!!498203658.jpg":{"w":'
    temp_str3 = r"https://item.taobao.com/item.htm?spm=a230r.1.14.27.379948f9AbDeiT&id=41119941557&ns=1&abbucket=16#detail"

    url = "https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-16801072333.25.610e793dECOm2Q&id=43649469372"
    url = "https://item.taobao.com/item.htm?spm=a230r.1.14.27.6b8f110eeYGAVb&id=24181980727&ns=1&abbucket=14#detail"
    url = "https://item.taobao.com/item.htm?spm=a230r.1.14.27.379948f9AbDeiT&id=41119941557&ns=1&abbucket=16#detail"
    html = mnet.get_html(url)

    img_info_url = tb_re.get_img_info_url_from_html(html)
    sid = tb_re.get_sid_from_img_info_url(img_info_url)
    detail_img_info_json = mnet.get_html(img_info_url)
    detail_img_urls = tb_re.get_all_detail_pic_url_from_json(detail_img_info_json, sid)
    download_pics(detail_img_urls, '3详情图')

    zhu_tu_urls = tb_re.get_zhutu_urls_from_string(html)
    download_pics(zhu_tu_urls, '1主图')

    fen_lei_pic_urls = tb_re.get_fen_lei_urls_from_string(html)
    download_pics(fen_lei_pic_urls, '2颜色分类')

    # temp = 1
    # for detail_img_url in detail_img_urls:
    #     mnet.download_img(r"d:/downPics/", detail_img_url, "详情图" + str(temp))
    #     temp += 1
    #
    # zhu_tu_urls = tb_re.get_zhutu_urls_from_string(html)
    # temp = 1
    # for zhu_tu_url in zhu_tu_urls:
    #     mnet.download_img(r"d:/downPics/", zhu_tu_url, "主图" + str(temp))
    #     temp += 1



    print("successed!")