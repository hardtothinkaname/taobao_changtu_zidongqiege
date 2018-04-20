import re
import my_network.my_net as mynet


def get_img_info_url_from_html(html_str):
    # 获取可以得到详情页图片的url
    # detail_pic_url_json_temple = '{"api":{"descUrl":"//dsc.taobaocdn.com/i8/520/960/525966028916/TB1PVfskbuWBuNjSszg8qv8jVla.desc%7Cvar%5Edesc%3Bsign%5E113649370e2d5dfe8134484f16e73064%3Blang%5Egbk%3Bt%5E1523246706","fetchDcUrl":"//hdc1.alicdn.com/asyn.htm?pageId=1058949233&userId=2263353395","httpsDescUrl":"//desc.alicdn.com/i8/520/960/525966028916/TB1PVfskbuWBuNjSszg8qv8jVla.desc%7Cvar%5Edesc%3Bsign%5E113649370e2d5dfe8134484f16e73064%3Blang%5Egbk%3Bt%5E1523246706"},"apiAddCart":"//cart.taobao.com/add_cart_item.htm?item_id=525966028916","apiBeans":"//count.taobao.com/counter3?keys=SM_368_dsr-2263353395,ICCP_1_525966028916","apiBidCount":"//tbskip.taobao.com/json/show_bid_count.htm?itemNumId=525966028916&old_quantity=195973&date=1523413827000","apiItemViews":"//count.taobao'
    pattern = r'"api":{"descUrl":"//(.*?)"'
    r = re.findall(pattern, html_str)
    api_img_info_url = r[0]
    return api_img_info_url


def get_all_detail_pic_url_from_json(json_str, sid=""):
    # 获取可以得到详情页图片的url
    detail_pic_url_json_temple = ' <img align="absmiddle" src="https://img.alicdn.com/imgextra/i2/2263353395/TB23WFotmFjpuFjSspbXXXagVXa_!!2263353395.jpg">'
    pattern = r'<img align="absmiddle" src="(.*?jpg|png)'
    r = re.findall(pattern, json_str)
    # all_item = []
    # for obj in r:
    #     pic_name = obj[0] + obj[1]
    #     url = "http://gdp.alicdn.com/imgextra/i1/" + sid + "/" + pic_name
    #     all_item.append(url)
    return r

def get_sid_from_img_info_url(img_info_url):
    # 天猫中没有用到这个，直接返回空就好
    return ""

# 获取主图
def get_zhutu_urls_from_string(html_str):
    # <a href="#"><img src="//img.alicdn.com/imgextra/i3/TB1PKWVPpXXXXXwaXXXXXXXXXXX_!!0-item_pic.jpg_60x60q90.jpg" /></a>
    pattern = r'//(.*?)_60x60q90.jpg'
    rs = re.findall(pattern, html_str)
    urls = []
    for r in rs:
        url = 'https://' + r
        urls.append(url)
    return urls


# 获取分类图
def get_fen_lei_urls_from_string(html_str):
    # temp_str = r'<a href="#" style="background:url(//img.alicdn.com/imgextra/i3/2263353395/TB2GMXorVXXXXX6XpXXXXXXXXXX_!!2263353395.jpg_40x40q90.jpg) center no-repeat;">'
    pattern = r'//(.*?)_40x40q90.jpg'
    rs = re.findall(pattern, html_str)
    urls = []
    for r in rs:
        url = 'https://' + r
        urls.append(url)
    return urls


if __name__ == '__main__':


    # html_str_data = ""
    # with open(r"D:\pythonProject\taobao_changtu_zidongqiege\business_re\tianmao_xiangqing_temple.html", mode='r', encoding='gbk', errors='ignore') as html_file:
    #     html_str_data = html_file.read()
    # # 读取天猫网页成功，测试于2018-4-16 12:57:47


    # zhutu_test_temple = r'<a href="#"><img src="//img.alicdn.com/imgextra/i3/TB1PKWVPpXXXXXwaXXXXXXXXXXX_!!0-item_pic.jpg_60x60q90.jpg" /></a>'
    # zhutu_urls = get_zhutu_urls_from_string(zhutu_test_temple)
    # # 提取主力地址成功，测试于2018-4-16 13:03:16


    # fenlei_test_temp = r'<a href="#" style="background:url(//img.alicdn.com/imgextra/i3/2263353395/TB2GMXorVXXXXX6XpXXXXXXXXXX_!!2263353395.jpg_40x40q90.jpg) center no-repeat;">'
    # fenlei_urls = get_fen_lei_urls_from_string(fenlei_test_temp)
    ## 提取分类地址成功，测试于2018-4-16 13:09:12


    detail_pic_url_temple = '{"api":{"descUrl":"//dsc.taobaocdn.com/i8/520/960/525966028916/TB1PVfskbuWBuNjSszg8qv8jVla.desc%7Cvar%5Edesc%3Bsign%5E113649370e2d5dfe8134484f16e73064%3Blang%5Egbk%3Bt%5E1523246706","fetchDcUrl":"//hdc1.alicdn.com/asyn.htm?pageId=1058949233&userId=2263353395","httpsDescUrl":"//desc.alicdn.com/i8/520/960/525966028916/TB1PVfskbuWBuNjSszg8qv8jVla.desc%7Cvar%5Edesc%3Bsign%5E113649370e2d5dfe8134484f16e73064%3Blang%5Egbk%3Bt%5E1523246706"},"apiAddCart":"//cart.taobao.com/add_cart_item.htm?item_id=525966028916","apiBeans":"//count.taobao.com/counter3?keys=SM_368_dsr-2263353395,ICCP_1_525966028916","apiBidCount":"//tbskip.taobao.com/json/show_bid_count.htm?itemNumId=525966028916&old_quantity=195973&date=1523413827000","apiItemViews":"//count.taobao'
    img_info_url = get_img_info_url_from_html(detail_pic_url_temple)
    ## 提取能获得详情页图片的地址成功，测试于2018-4-16 14:14:35

    # ============================================================以上已测试完======================================================================================

    detail_pic_json = mynet.get_html(img_info_url)
    detail_pic_url_json_temple = ' <img align="absmiddle" src="https://img.alicdn.com/imgextra/i2/2263353395/TB23WFotmFjpuFjSspbXXXagVXa_!!2263353395.jpg">'
    detail_pic_urls = get_all_detail_pic_url_from_json(detail_pic_json)
    ##从返回的json中提取url成功，测试于2018-4-16 15:23:02

    print("tianmao_re, test is complete!")
