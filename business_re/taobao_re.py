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


# 获取主图，根据关键字_50x50.jpg
def get_zhutu_urls_from_string(html_str):
    # temp_str = r'<a href="#"><img data-src="//gd2.alicdn.com/imgextra/i1/1798680826/TB2sOVXa0knBKNjSZKPXXX6OFXa_!!1798680826.jpg_50x50.jpg" /'
    pattern = r'//(.*?)_50x50.jpg'
    rs = re.findall(pattern, html_str)
    urls = []
    for r in rs:
        url = 'https://' + r
        urls.append(url)
    return urls


# 获取分类图，根据关键字_30x30.jpg
def get_fen_lei_urls_from_string(html_str):
    # temp_str = r'<a href="javascript:;" style="background:url(//gd1.alicdn.com/imgextra/i3/1798680826/TB2ahuTcx9YBuNjy0FfXXXIsVXa_!!1798680826.jpg_30x30.jpg) center no-repeat;">'
    pattern = r'//(.*?)_30x30.jpg'
    rs = re.findall(pattern, html_str)
    urls = []
    for r in rs:
        url = 'https://' + r
        urls.append(url)
    return urls


# 获取分类的字
def get_fen_lei_text_from_str(html_str):
    pattern = r'<li data-value=.*?<span>(.*?)</span>'
    return_str = re.findall(pattern, html_str, re.S)
    return return_str

# 提取获取价格的地址
def get_price_url_from_html(html_str):
    pattern = r"wholeSibUrl      : '//(.*?)'"
    return_str = re.findall(pattern, html_str)
    return return_str[0]

if __name__ == '__main__':
    temp_str = r'<a href="#"><img data-src="//gd2.alicdn.com/imgextra/i1/1798680826/TB2sOVXa0knBKNjSZKPXXX6OFXa_!!1798680826.jpg_50x50.jpg" /'
    re_str = get_zhutu_urls_from_string(temp_str)

    temp_str2 = r'<a href="javascript:;" style="background:url(//gd1.alicdn.com/imgextra/i3/1798680826/TB2ahuTcx9YBuNjy0FfXXXIsVXa_!!1798680826.jpg_30x30.jpg) center no-repeat;">'
    re_str2 = get_fen_lei_urls_from_string(temp_str2)


    temp_str3 = r'<ul data-property="颜色分类" class="J_TSaleProp tb-img tb-clearfix"><li data-value="1627207:431809108" class="tb-txt"><a href="javascript:void(0);"><span>30CM挂轴一对</span></a><i>已选中</i></li>'

    re.findall()

    print("done!")

