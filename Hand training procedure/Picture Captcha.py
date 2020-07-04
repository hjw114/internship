from PIL import Image, ImageDraw, ImageFont  # 引入绘图模块
import random  # 引入随机函数模块


def get_random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


def make_captcha():
    # 定义变量，宽，高，背景颜色
    width = 200
    height = 50
    background_color = get_random_color()
    image = Image.new('RGB', (width, height), background_color)    # 创建画布
    draw = ImageDraw.Draw(image)   # 创建画板

    # 调用画板的point()函数绘制杂点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        draw.point(xy, fill = get_random_color())

    # 调用画板的line()函数制杂线
    for i in range(0, 10):
        xy_start = (random.randrange(0, width), random.randrange(0, height))
        xy_end = (random.randrange(0, width), random.randrange(0, height))
        draw.line((xy_start, xy_end), fill = get_random_color())

    # 用draw.text书写文字
    rand_captcha = ''
    for i in range(4):
        random_number = str(random.randint(0, 9))
        random_lower_letter = chr(random.randint(97, 122))
        random_upper_letter = chr(random.randint(65, 90))
        rand_captcha += random.choice([random_number, random_lower_letter, random_upper_letter,])
        color = get_random_color()
        text_color = [0, 0, 0]

        # 保证文字颜色与背景颜色不要太接近
        for j in range(3):
            if color[j]-background_color[j] <= 30:
                text_color[j] = 255-color[j]
            else:
                text_color[j] = color[j]

        try:
            draw.text((i * (width/4) + 10, 2),
                  rand_captcha[i],
                  tuple(text_color),
                  font=ImageFont.truetype(r'C:\Windows\Fonts\BRADHITC.TTF', 40),
                  align='center')
        except OSError:
            print("你的C:\Windows\Fonts目录下没有BRADHITC.TTF字体文件，赶紧去代码里修改一下你有的字体文件吧")
            break

    image.save("验证码.png")


# 主函数
if __name__ == '__main__':
    make_captcha()
    print("验证码图片已生成在程序当前运行目录下")