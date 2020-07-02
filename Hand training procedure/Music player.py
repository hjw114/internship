import pygame
import sys
import os
class button:#按钮属性
    def __init__(self,screen,msg,x,y,t):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.width,self.height=300,50
        self.x,self.y=x,y
        self.button_color=(255,255,255)
        self.text_color=(255,200,10)
        self.font=pygame.font.SysFont('microsoft Yahei', t)
        self.rect=pygame.Rect(x,y,self.width,self.height)
        self.prep_msg(msg)
    def prep_msg(self,msg):#将msg渲染为图像，并使其在按钮上居中
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    def draw_button(self):# 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
def serch(position):#遍历查找文件
    i=0;
    threefile=[]
    for file in os.listdir(position):
        if os.path.splitext(file)[1] == '.mp3':
            sourcefile = os.path.join(position, file)  # 拼路径
            threefile.append(sourcefile)
            i=i+1
    return threefile,int(i)
def printScale(text,P):#调节音量
    t=float(text)
    u = pygame.mixer.music.get_volume()
    if P=="T":
        pygame.mixer.music.set_volume(u + t)
    else:
        pygame.mixer.music.set_volume(u - t)
def FONT(size):#调节字体大小
    t=int(size)
    return pygame.font.SysFont('microsoft Yahei', t)
def mousposition():#获取鼠标位置
    return pygame.mouse.get_pos()
def mousepress(x,y,i,t):#判断是否点击
    if Up.rect.collidepoint(x,y):
        printScale(0.1,"T")
    elif Down.rect.collidepoint(x,y):
        printScale(0.1,"F")
    elif Pause.rect.collidepoint(x,y):
        pygame.mixer.music.pause()
    elif Start.rect.collidepoint(x,y):
        pygame.mixer.music.unpause()
    elif Last.rect.collidepoint(x,y):
        if t==0:
            pygame.mixer.music.rewind()
            return t
        else:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(catalog[t-1])
            pygame.mixer.music.play()
            return t-1
    elif Next.rect.collidepoint(x,y):
        if t==i-1:
            pygame.mixer.music.rewind()
            return t
        else:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(catalog[t+1])
            pygame.mixer.music.play()
            return t+1
def run():
    t=0
    pygame.time.delay(1000)
    pygame.mixer.music.load(catalog[t])
    pygame.mixer.music.play()
    while True:
        for event in pygame.event.get():#检测行为
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                (x,y)=mousposition()
                t=mousepress(x,y,i,t)
        pygame.display.flip()


position = input("请输入歌曲位置（上级目录，MP3格式）:")
(catalog,i)=serch(position)
pygame.init()  # 启动pygame
screen = pygame.display.set_mode([1200, 800])
Title=button(screen,"Music player",100,100,60)
Up=button(screen,"Volume up",500,100,30)
Down=button(screen,"Volume down",900,100,30)
Pause=button(screen,"Pause",250,500,30)
Start=button(screen,"Start",650,500,30)
Last=button(screen,"Last song",250,700,30)
Next=button(screen,"Next song",650,700,30)
Title.draw_button()
Up.draw_button()
Down.draw_button()
Pause.draw_button()
Start.draw_button()
Last.draw_button()
Next.draw_button()
run()