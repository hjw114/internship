import Conversion_value
import Sorting
import Graying
import Regional_segmentation
import cv2


class Picture:#图片类，父类
    def __init__(self,route):#属性函数
        self.route=route
    def imshow(self,name):#显示图片
        cv2.imshow(name,cv2.imread(self.route,cv2.IMREAD_UNCHANGED))
        cv2.waitKey()
    def preservation(self,name):#保存图片
        cv2.imwrite(self.route,name)


route=input("请输入图像的位置：")
picture=Picture(route)
picture.imshow(picture)
conversion=Conversion_value.conversion_value(picture)#二值化函数
sort=Sorting.sorting(conversion)#排序函数
gray=Graying.graying(sort)#灰度化函数
regional=Regional_segmentation.regional_segmentation(gray)#图像分割函数


#此文件为协议文件，作为总项目的控制文件，功能文件名见导入类。每个功能文件继承或使用本文件中的类进行复写。
# 本文件中的类中的功能必须每个文件都实现一遍，文件中各个功能的实现函数同样必须实现。
#排序函数需要在控制台打印出排序结果
#分割函数需要在控制台打印出分割依据或分割目标或其他分割标志