# 处理图片，自动切割
# 原理：通过每一横的图像波动率来检查些是否应该此是切割处。

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

if __name__ == "__main__":
    file_path = r"D:\门型架\3详情图2_TB2vf5cgY_I8KJjy1XaXXbsxpXa_!!1071327275.jpg"
    # file_path = r"D:\门型架\3详情图1_TB2lcc5vYBmpuFjSZFAXXaQ0pXa_!!1071327275.jpg"
    img = np.array(Image.open(file_path))
    # plt.imshow(img)
    # plt.axis('off')
    # plt.show()

    meanx = img.mean(axis=1)
    row_1 = img[:, 1, :]
    # 平均值与列头相减
    row_sub = row_1 - meanx
    # 三颜色相加
    row_sub_add_chanel = row_sub[:, 0][:] + row_sub[:, 1][:] + row_sub[:, 2][:]
    binary_row = np.array(list(map(lambda x: (0, 1)[abs(x) < 0.01], row_sub_add_chanel)))

    # 检查从哪里单色开始到结束
    lines_arr = []
    start_flag = True
    last_x = 0
    single_lines_sum = 0
    row_num = 0
    for x in binary_row:
        row_num += 1
        if last_x == 0 and x == 1:
            # 纯色横线开始
            start_flag = True
            single_lines_sum += 1

        if last_x == 1 and x == 1:
            single_lines_sum += 1

        if (last_x == 1 and x == 0) or row_num == binary_row.shape[0]:
            # 纯色横线开始
            start_flag = False
            mid_line = (int)(row_num - (single_lines_sum / 2))
            single_lines_sum = 0
            lines_arr.append(mid_line)

        last_x = x

    # 假如第一行不是1，则添加为1
    if lines_arr[0] != 1:
        lines_arr.insert(0, 1)

    last_line = -1
    for line in lines_arr:
        if last_line == -1:
            last_line = line
            continue
        new_img = img[last_line:line, :, :]
        plt.imshow(new_img)
        plt.show()
        last_line = line
        print("")

    print(binary_row.shape[0])
    print(lines_arr)
    print("binary_row type,", binary_row)
    print("wub", row_sub[:, 0][:])
    print("row1.shape", row_1.shape)
    print(img.shape)
    print(img.dtype)
    print(img.size)
    print(type(img))

    print("done,pic segment")
