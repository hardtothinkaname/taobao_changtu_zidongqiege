# import numpy as np
# from matplotlib import pyplot as plt
import urllib3
import re
from my_network import my_net as mnet
import tao_bao_re as tb_re


if __name__ == '__main__':

    temp_str = r"111apiImgInfo  : '//tds.alicdn.com/json/item_imgs.htm?t=TB1cAiFiv5TBuNjSspmXXaDRVXa&sid=498203658&id=24181980727&s=f56a9247beacb582a03a0c6661d6a8bc&v=2&m=1',"
    temp_str2 = r'!498203658.jpg":{"w":750, "h":1060},"TB2FYiltVXXXXaKXXXXXXXXXXXX-498203658.jpg":{"w":750, "h":844},"TB2aWR0sYFlpuFjy0FgXXbRBVXa_!!498203658.jpg":{"w":'
    temp_str3 = r"http://gdp.alicdn.com/imgextra/i1/498203658/TB2_lags3FkpuFjSspnXXb4qFXa_!!498203658.jpg"

    url = "https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-16801072333.25.610e793dECOm2Q&id=43649469372"
    html = mnet.get_html(url)
    img_info_url = tb_re.get_img_info_url_from_html(html)
    sid = tb_re.get_sid_from_img_info_url(img_info_url)
    detail_img_info_json = mnet.get_html(img_info_url)
    detail_img_urls = tb_re.get_all_detail_pic_url_from_json(detail_img_info_json, sid)

    temp = 1
    for img_url in detail_img_urls:
        mnet.download_img(r"d:/downPics/", img_url, "详情图" + str(temp))
        temp += 1


    # print("ss")