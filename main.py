# import numpy as np
# from matplotlib import pyplot as plt
import urllib3
import re

urllib3.disable_warnings()
http = urllib3.PoolManager()


def get_html(url):
    r = http.request('GET', url)
    return r.data.decode("gbk", "ignore")


def download_img(path, url, prefix_name=""):
    mkdir(path)
    name = re.split("/", url)
    name = prefix_name + "_" + name[len(name) - 1]
    path = path + name
    r = http.request('GET', url, preload_content=False)
    with open(path, 'wb') as out:
        while True:
            data = r.read()
            if not data:
                break
            out.write(data)


def get_img_info_url_from_html(html_str):
    # 获取可以得到详情页图片的url
    pattern = r"apiImgInfo.*',"
    r = re.search(pattern, html_str)
    sp = r.span()
    api_img_info_url = html_str[sp[0] + 15: sp[1] - 2]
    return "https:" + api_img_info_url


def get_all_detail_pic_url_from_json(json_str, sid):
    # 获取可以得到详情页图片的url
    pattern = r',"(.*?)(jpg|png)"'
    r = re.findall(pattern, json_str)
    all_item = []
    for obj in r:
        pic_name = obj[0] + obj[1]
        url = "http://gdp.alicdn.com/imgextra/i1/" + sid + "/" + pic_name
        all_item.append(url)
    return all_item


def get_sid_from_img_info_url(img_info_url):
    pattern = r'sid=.*?&'
    r = re.findall(pattern, img_info_url)
    sid = r[0][4: -1]
    return sid


def mkdir(path):
    # 引入模块
    import os
    path = path.strip()
    path = path.rstrip("\\")
    is_exists = os.path.exists(path)
    if not is_exists:
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        return False


if __name__ == '__main__':

    temp_str = r"111apiImgInfo  : '//tds.alicdn.com/json/item_imgs.htm?t=TB1cAiFiv5TBuNjSspmXXaDRVXa&sid=498203658&id=24181980727&s=f56a9247beacb582a03a0c6661d6a8bc&v=2&m=1',"
    temp_str2 = r'!498203658.jpg":{"w":750, "h":1060},"TB2FYiltVXXXXaKXXXXXXXXXXXX-498203658.jpg":{"w":750, "h":844},"TB2aWR0sYFlpuFjy0FgXXbRBVXa_!!498203658.jpg":{"w":'
    temp_str3 = r"http://gdp.alicdn.com/imgextra/i1/498203658/TB2_lags3FkpuFjSspnXXb4qFXa_!!498203658.jpg"

    url = "https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-16801072333.25.610e793dECOm2Q&id=43649469372"
    html = get_html(url)
    # html_str = html.decode("gbk", "ignore")
    img_info_url = get_img_info_url_from_html(html)
    sid = get_sid_from_img_info_url(img_info_url)
    detail_img_info_json = get_html(img_info_url)
    detail_img_urls = get_all_detail_pic_url_from_json(detail_img_info_json, sid)

    temp = 1
    for img_url in detail_img_urls:
        download_img(r"d:/downPics/", img_url, "详情图" + str(temp))
        temp += 1


    print("ss")