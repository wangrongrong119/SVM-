# SVM-舌头训练：

1.图虫爬虫 输入人脸 舌头， requests模块
2.图片预处理 ，
2.1人脸检测 ，扣出人脸   opencv 里自带模型 ， 
Java实现 https://blog.csdn.net/c_molione/article/details/80831286
参考了：Python实现 https://blog.csdn.net/haohuajie1988/article/details/79163318
2.2 图片批量重命名，resize, 
img = cv2.resize(img, (100,128))
listStr = ['face', str(count)]
fileName = ''.join(listStr)
cv2.imwrite(object+os.sep+'%s.jpg' % fileName, img)

3.SVM训练 
正确率0.66


数据增强   图像对应的list的生成
参考了
https://blog.csdn.net/weixin_34218890/article/details/87454323
数据增强后0.456
