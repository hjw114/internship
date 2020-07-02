import os
import time

from tkinter import filedialog,Tk
from PIL import Image, ImageTk
import tkinter



class Application():
    def __init__(self, root):
        self.files = self.get_pic_path()
        self.index = 0
        image=Image.open(self.files[self.index])
        width,height=self.auto_scale(image)
        pic_image = image.resize((width, height), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(image=pic_image)
        self.root = root
        self.createLable()
    def auto_scale(self, pic_image):
        """自动缩放"""
        width, height = pic_image.size  # 获取图片的width height
        org_rate = width / height
        if width > height:
            # 宽缩放
            rate = 1
            while True:
                scale_width = width * rate
                if scale_width <= 1080:
                    break
                rate -= 0.1
            scale_height = scale_width / org_rate
            return int(scale_width), int(scale_height)
        else:
            # 高缩放
            rate = 1
            while True:
                scale_height = height * rate
                if scale_height <= 720:
                    break
                rate -= 0.1
            scale_width = scale_height * org_rate
            return int(scale_width), int(scale_height)
    def createLable(self):
        self.pic_lable = tkinter.Label(self.root, width=1080, height=720)
        self.pic_lable['image'] = self.img
        self.pic_lable.pack()
    def get_pic_path(self):
        path = filedialog.askdirectory()
        pic_list = [''.join([path, '/', img]) for img in os.listdir(path)]
        return pic_list
    def get_ico(self, path):
        ico_img = Image.open(path).resize((32, 32))
        icoBtn = ImageTk.PhotoImage(image=ico_img)
        return icoBtn
    def prev(self):
        self.show_file(-1)

    def next(self):
        self.show_file(1)

    def show_file(self, n):
        self.index += n
        if self.index < 0:
            self.index = len(self.files) - 1
        if self.index > (len(self.files) - 1):
            self.index = 0
        image=Image.open(self.files[self.index])
        width,height=self.auto_scale(image)
        pic_image = image.resize((width, height), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(image=pic_image)
        self.pic_lable['image'] = self.img
    def auto_play(self):
        """自动播放图片"""
        for i in range(len(self.files)):
            self.index = i
            pic_image = Image.open(self.files[self.index])
            width, height = self.auto_scale(pic_image)
            pic = pic_image.resize((width, height), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(image=pic)
            self.pic_lable['image'] = self.img
            self.pic_lable.pack()
            self.pic_lable.update()
            time.sleep(1)

root = Tk()
root.title('PIC-Player')
root.geometry("1080x720")
root['bg'] = '#333333'
root.resizable(False, False)
root.iconbitmap(r'D:\图片浏览器\22.png')

app= Application(root)
def auto_play():
    app.auto_play()
pr = app.get_ico(r'D:\图片浏览器\23.png')
nt = app.get_ico(r'D:\图片浏览器\24.png')
btnPrev = tkinter.Button(root, image=pr, command=app.prev)
btnPrev.place(x=-10, y=360)
btnNext = tkinter.Button(root, image=nt, command=app.next)
btnNext.place(x=1050, y=360)
auto_play()
root.mainloop()
