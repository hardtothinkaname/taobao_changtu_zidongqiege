import re


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