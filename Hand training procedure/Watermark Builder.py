import os
from PIL import Image, ImageFont, ImageDraw

# 添加文字水印
def txtmark(img, num, watermark):
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))  # 新建一个空白图片,大小与打开图片相同
    pic2 = ImageDraw.Draw(layer)  # 将新建的图片添入画板
    pic2.text((layer.size[0] - 115, layer.size[1] - 80), watermark, font = ft, fill = 'white') # 在画板上添加水印
    out = Image.alpha_composite(img, layer)  # 合并两个图片
    out = out.convert('RGB')
    out.save(str(num) +".jpg")

# 添加图片水印
def picmark(img, num, watermark):
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))  # 新建一个空白图片,大小与打开图片相同
    mark = Image.open(watermark)    # 打开水印图片
    if (layer.size[0] < mark.size[0]) or (layer.size[1] < mark.size[1]):
        print("兄die，水印比图片大了")
    else:
        layer.paste(mark, (layer.size[0] - mark.size[0], layer.size[1] - mark.size[1]))  # 在画板上添加水印
        out = Image.composite(layer, img, layer)  # 合并两个图片
        out = out.convert('RGB')
        out.save(str(num)+ ".jpg")

answer = 1
while answer:
    picturepath = input("请输入需要添加水印的图片的文件夹名（绝对路径）: ")
    temp = input("图片水印输入0，文字水印输入1： ")
    watermark = input("请输入水印图片文件绝对路径（带后缀名）/水印文字内容: ")

    try:
        ft=ImageFont.truetype("c:/Windows/Fonts/SIMYOU.ttf", 40)    # 设置水印字体
    except OSError:
        print("提供的路径出错了，换个路径吧（可能是路径包含了中文）")
    else:
        i = 0
        img_suffix_list = ['png', 'jpg', 'bmp']
        answer = 0
        for files in os.listdir(picturepath):
            if files.split('.')[-1] in img_suffix_list:     # 选择图片文件
                try:
                    im = Image.open(files).convert('RGBA')    # 打开待处理图片
                except FileNotFoundError:
                    print("请把目标文件夹里的隐藏后缀名取消掉，不然不能运行")
                    answer = 1
                    break
                else:
                    i += 1
                    if int(temp):
                        txtmark(im, i, watermark)
                    else:
                        picmark(im, i, watermark)
