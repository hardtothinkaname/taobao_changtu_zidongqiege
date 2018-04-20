import urllib3
import re
import urllib.request

urllib3.disable_warnings()
http = urllib3.PoolManager()


def get_html(url, coding="gbk"):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"

    }
    r = http.request('GET', url, headers=headers, retries=5, redirect=500)
    return r.data.decode(coding, "ignore")


def get_html_with_referer(url, referer, coding="gbk"):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
        "Referer": referer
    }
    r = http.request('GET', url, headers=headers, retries=5, redirect=500)
    return r.data.decode(coding, "ignore")

def get_html2(url):
    r = urllib.request.urlopen(url).read()
    return r.decode("gbk", "ignore")


def download_img(path, url, prefix_name=""):
    create_folder(path)
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


def create_folder(path):
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
    url = "https://detail.1688.com/offer/561345651056.html?spm=a261y.7663282.0.0.d59b588aI9fP4t"
    # 淘宝店，测试
    url = "https://item.taobao.com/item.htm?spm=a230r.1.14.48.131e6ab3LJeKpP&id=529747601133&ns=1&abbucket=14#detail"

    # 天猫店，测试
    # url = "https://detail.tmall.com/item.htm?spm=a220o.1000855.1998025129.3.69ed6698tAXrQR&abtest=_AB-LR32-PR32&pvid=2526ea32-267e-4e7a-9e8f-05ca1a1b25ed&pos=3&abbucket=_AB-M32_B19&acm=03054.1003.1.2768562&id=525966028916&scm=1007.16862.95220.23864_0"

    # 天猫详情中的图片连接
    # url = r'dsc.taobaocdn.com/i8/520/960/525966028916/TB1PVfskbuWBuNjSszg8qv8jVla.desc%7Cvar%5Edesc%3Bsign%5E113649370e2d5dfe8134484f16e73064%3Blang%5Egbk%3Bt%5E1523246706'

    url2 = "https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=529747601133&sellerId=2178947922&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract"


    html = get_html_with_referer(url2, url)
    print("helo")
