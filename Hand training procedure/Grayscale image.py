"""
导入图片并存成灰度图，根据输入参数调整对比度及亮度，进行颜色取反
使用时需要修改图片路径
"""
import cv2
import numpy as np

def gray(img):
    #灰度图处理
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imshow("img_gray", img_gray)
    return img_gray

def Contrast_and_Brightness(alpha, beta, img):
    # 调整对比度和亮度
    rows, cols, channels = img.shape  # 获得图像的长、宽、通道
    img_contrast = img.copy()  # 图像复制
    for i in range(rows):
        for j in range(cols):
            for c in range(3):
                color = img[i, j][c] * alpha+ beta
                if color > 255:  # 防止像素值越界（0~255）
                    img_contrast[i, j][c] = 255
                elif color < 0:  # 防止像素值越界（0~255）
                    img_contrast[i, j][c] = 0
    cv2.imshow("img_contrast", img_contrast)
    return img_contrast

def inverse(img):
	#颜色取反
    img_inverse = cv2.bitwise_not(img)
    cv2.imshow("颜色取反",img_inverse)
    cv2.waitKey()
    return img_inverse

if __name__ == "__main__":
    img_path = "D:/Python Project/demo2/venv/qq_icon.PNG"
    img = cv2.imread(img_path)  # 图片读取
    cv2.imshow("img", img)  # 显示图片
    cv2.waitKey()
    img_gray = gray(img)
    cv2.waitKey()
    a, b = map(int, input('输入对比度和亮度参数并空格隔开:').split())
    img_contrast = Contrast_and_Brightness(a,b,img)
    cv2.waitKey()
    img_inverse = inverse(img)
    cv2.imwrite("D:/Python Project/demo2/venv/img_gray.PNG", img_gray)  # 保存图片
    cv2.imwrite("D:/Python Project/demo2/venv/img_contrast.PNG", img_contrast)
    cv2.imwrite("D:/Python Project/demo2/venv/img_contrast.PNG", img_inverse)




