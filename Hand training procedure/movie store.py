class videotape:
    def __init__(self, name, price, ind, number):
        """
        录像带类：
        包括录像带的名字，买回来的价格，类别编号（电影类别），库存数量
        """
        self.name = name #名字
        self.price = price #价格
        self.number = number #编号
        self.ind = ind #库存数量

    def __str__(self):
        return 'name:%s,price:%s,cate_id:%s,number:%s' % (self.name, self.price, self.ind, self.number)

class bor_videotape:
    def __init__(self,video_name,video_id,user_id,time_bor,time_re,time_now,day):
        """
        被租借的录像带类
        """
        self.video_name=video_name #名称
        self.video_id=video_id #录像带id
        self.user_id=user_id #用户id
        self.time_bor=time_bor #借阅时间
        self.time_re=time_re #应还时间
        self.time_now=time_now
        self.day=day
    def __str__(self):
        return '录像带名称：%s|录像带id:%s|借录像带的人：%s|借阅时间：%s|应还时间:%s'%(self.video_name,self.video_id,self.user_id,self.time_bor,self.time_re)


class user:
    def __init__(self, name, ind=0, bor_report=[]):
        """
        借录像带的用户：
        包括用户的名字，id号，
        """
        self.name = name
        self.ind = ind
        self.bor_report = [] #用户租借的录像带

    def video_bor(self, bor_videotape, flag=1):
        """"
        判断是否超过可借录像带数目
        """
        if (len(self.bor_report) < 5 or flag == 0):
            if flag == 1:
                self.bor_report.append(bor_videotape)
                return 1
            else:
                self.bor_report.remove(bor_videotape)
                return 2
        else:
            print("超出可借电影带数目")
            return 0

    def n_video(self):
        return len(self.bor_report)

    def list_video(self):
        for i in range(len(self.bor_report)):
            print(self.bor_report[i])


class shop(object):
    """
    电影商店类：
    包括存放录像带的list
    """

    def __init__(self):

        self.video = []
        self.report = []
        self.overdue = []
        self.user = []
        self.day = 30

    def addVideo(self, videotape):

        """
        添加库存：
        如果有新进录像带，直接添加到原有库存中。
        不是新录像带则添加数量。
        """

        # 有库存
        if len(self.video) > 0:
            flag = 0
            for i in range(len(self.video)):
                if (self.video[i].ind == videotape.ind and self.video[i].name == videotape.name):
                    self.video[i].number += videotape.number
                    flag = 1
            if (flag != 1):
                self.video.append(videotape)
        # 无库存
        else:
            self.video.append(videotape)

    def adduser(self, user_name):
        """"
        添加用户
        """
        u = user(user_name, len(self.user) + 1)
        self.user.append(u)

    def List_video(self):
        """"
        录像带列表
        """
        for i in range(len(self.video)):
            print('录像带ID：%s | 录像带名称：%s | 录像带数量：%s | 录像带价格：%s' % (
            self.video[i].ind, self.video[i].name, self.video[i].number, self.video[i].price))

    def List_user(self):
        """"
        用户列表
        """
        for i in range(len(self.user)):
            print('用户名称：%s | 用户ID：%s | 已借录像带数：%s' % (self.user[i].name, self.user[i].ind, self.user[i].n_video()))

    def borrowVideo(self, video_l, user_ID, day):
        """"
        借阅录像带
        """
        flag = 0
        if (isinstance(video_l, int)):
            for i in range(len(self.video)):
                if (self.video[i].ind == video_l):
                    flag = 1
                    if (self.video[i].number == 0):
                        print('该录像带已全部借出！')
                        for i in range(len(self.report)):
                            print(i)
                            if (self.report[i].video_id == video_l):
                                print('录像带名称：%s|录像带id:%s|借阅人ID：%s|借阅时间：%s|应还时间:%s' % (
                                self.report[i].video_name, self.report[i].video_id, self.report[i].user_id,
                                self.report[i].time_bor, self.report[i].time_re))
                    else:
                        re = bor_videotape(self.video[i].name, self.video[i].ind, user_ID, day, self.day + day, day, 0)
                        self.report.append(re)
                        flag1 = self.user[user_ID - 1].video_bor(re)
                        if (flag1 == 1):
                            self.video[i].number -= 1
                        print('用户名称：%s | 用户ID：%s | 已借录像带数：%s' % (
                        self.user[user_ID - 1].name, self.user[user_ID - 1].ind, self.user[user_ID - 1].n_video()))

            if (flag == 0):
                print("库存中没有该录像带！！")
        else:
            for i in range(len(self.video)):
                if (self.video[i].name == video_l):
                    flag = 1
                    if (self.video[i].number == 0):
                        print('该录像带已全部借出！')
                        for i in range(len(self.report)):
                            if (self.report[i].video_name == video_l):
                                print('录像带名称：%s|录像带id:%s|借阅人ID：%s|借阅时间：%s|应还时间:%s' % (
                                self.report[i].video_name, self.report[i].video_id, self.report[i].user_id,
                                self.report[i].time_bor, self.report[i].time_re))
                    else:
                        re = bor_videotape(self.video[i].name, self.video[i].ind, user_ID, day, self.day + day, day, 0)
                        self.report.append(re)
                        flag1 = self.user[user_ID - 1].video_bor(re)
                        if (flag1 == 1):
                            self.video[i].number -= 1
                        print('用户名称：%s | 用户ID：%s | 已借录像带数：%s' % (
                        self.user[user_ID - 1].name, self.user[user_ID - 1].ind, self.user[user_ID - 1].n_video()))

            if (flag == 0):
                print("库存中没有该录像带！！")
        self.overduereport_update(day)
        self.user[user_ID - 1].list_video()

    def returnVideo(self, video_l, user_l, day):
        """"
        归还录像带
        """
        self.overduereport_update(day)
        if (isinstance(video_l, int)):
            for i in range(len(self.report)):
                if (self.report[i].video_id == video_l and self.report[i].user_id == user_l):
                    self.report.remove(self.report[i])
                    re = self.report[i]
                    self.user[user_l - 1].video_bor(re)
            for i in range(len(self.overdue)):
                if (self.overdue[i].video_id == video_l and self.overdue[i].user_id == user_l):
                    print('录像带名称：%s|录像带id:%s|借阅人ID：%s|借阅时间：%s|应还时间:%s|逾期时间：%s' % (
                    self.overdue[i].video_name, self.overdue[i].video_id, self.overdue[i].user_id,
                    self.overdue[i].time_bor, self.overdue[i].time_re, self.overdue[i].day))
                    self.overdue.remove(self.overdue[i])
            self.video[i].number += 1
        else:
            for i in range(len(self.report)):
                if (self.report[i].video_name == video_l and self.report[i].user_id == user_l):
                    self.report.remove(self.report[i])
            for i in range(len(self.overdue)):
                if (self.overdue[i].video_name == video_l and self.overdue[i].user_id == user_l):
                    self.overdue.remove(self.overdue[i])
            self.video[i].number += 1

    def list_report(self):
        for i in range(len(self.report)):
            print('录像带名称：%s|录像带id:%s|借阅人ID：%s|借阅时间：%s|应还时间:%s' % (
            self.report[i].video_name, self.report[i].video_id, self.report[i].user_id, self.report[i].time_bor,
            self.report[i].time_re))

    def overduereport_update(self, day):
        self.overdue = []
        for i in range(len(self.report)):
            if ((day - self.report[i].time_bor) > self.day):  # 逾期
                self.overdue.append(self.report[i])

    def overduereport(self, day):
        self.overduereport_update(day)
        for i in range(len(self.overdue)):
            print('录像带名称：%s|录像带id:%s|借阅人ID：%s|借阅时间：%s|应还时间:%s|逾期时间：%s' % (
            self.overdue[i].video_name, self.overdue[i].video_id, self.overdue[i].user_id, self.overdue[i].time_bor,
            self.overdue[i].time_re, self.overdue[i].day))

s=shop()
v1=videotape("1",50,1001,10)
v2=videotape("2",20,1002,5)
v3=videotape("3",30,1003,15)
s.addVideo(v1)
s.addVideo(v2)
s.addVideo(v3)
s.List_video()
print()
s.adduser("小A")
s.adduser("小B")
s.List_user()
print()
s.borrowVideo(1001,1,3)
print()
s.borrowVideo(1002,2,4)
print()
s.List_video()
print()
s.list_report()
print()

s.returnVideo(1,1,2)
s.List_video()
print()
s.returnVideo(2,2,5)
s.List_video()
print()



