import urllib3
import re

urllib3.disable_warnings()
http = urllib3.PoolManager()


def get_html(url):
    r = http.request('GET', url)
    return r.data.decode("gbk", "ignore")


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
