# -*- coding: UTF-8 -*-
import os
from PIL import Image
from PIL import ImageEnhance


# 原始图像
def ImageAugument():
    path = "C:/Users/19482/Desktop/wrr/HOG_SVM-master/image128"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    # 遍历文件夹
    prefix = path + '/'
    for file in files:
        image = Image.open(prefix + file)
        # image.show()

        # 亮度增强
        enh_bri = ImageEnhance.Brightness(image)
        brightness = 1.5
        image_brightened = enh_bri.enhance(brightness)
        image_brightened.save(prefix + file[0:6] + 'lightup' + '.jpg')

        # 色度增强
        enh_col = ImageEnhance.Color(image)
        color = 1.5
        image_colored = enh_col.enhance(color)
        image_colored.save(prefix + file[0:6] + 'colorup' + '.jpg')

        # 对比度增强
        enh_con = ImageEnhance.Contrast(image)
        contrast = 1.5
        image_contrasted = enh_con.enhance(contrast)
        image_contrasted.save(prefix + file[0:6] + 'contrastup' + '.jpg')

        # 锐度增强
        enh_sha = ImageEnhance.Sharpness(image)
        sharpness = 3.0
        image_sharped = enh_sha.enhance(sharpness)
        image_sharped.save(prefix + file[0:6] + 'moreSharp' + '.jpg')


if __name__ == '__main__':
    ImageAugument()
