import random
class Role:
    # 设定游戏角色名字
    def setName(self):
        while True:
            self.name = input("请输入您的游戏名并确保长度小于50：")
            if len(self.name) > 50:
                print("您的名字过长,请重新输入")
                continue
            break
        return self.name
    # 设定角色性别
    def setSex(self):
        while True:
            n = int(input("请选择您的角色性别：0：男，1：女"))
            if n == 0:
                self.sex = '男'
                break
            elif n == 1:
                self.sex = '女'
                break
            else:
                print("请在0或1之间选择！")
                continue
        return self.sex
    # 设定角色种族
    def setRace(self):
        while True:
            n = int(input("请选择您的角色种族：0：人类，1：精灵，2：兽人，3：矮人，4：元素"))
            if n not in range(0,5):
                print("请在0-5之间选择")
                continue
            Race = { 0: '人类',1: '精灵',2: '兽人',3: '矮人',4: '元素'}
            self.race = Race[n]
            break
        return self.race

    #设定角色属性
    def setAttribute(self):
        self.power = 0            #力量
        self.agile = 0            #敏捷
        self.strength = 0         #体力
        self.intelligence = 0     #智力
        self.wisdom = 0           #智慧
        self.life = 0             #生命值
        self.magicpoint = 0       #魔法值
        self.str=" "
        if self.race == '人类':
            self.power = random.randint(35,40)
            self.agile = random.randint(15,20)
            self.strength = random.randint(25,30)
            self.intelligence = random.randint(0,100-self.agile-self.strength)
            self.wisdom = 100-self.power-self.agile-self.strength-self.intelligence
        elif self.race == '精灵':
            self.power = random.randint(20,25)
            self.strength = random.randint(25,30)
            self.intelligence = random.randint(15,20)
            self.agile = random.randint(0, 100 - self.power - self.strength - self.intelligence)
            self.wisdom = 100-self.power-self.agile-self.strength-self.intelligence
        elif self.race == '兽人':
            self.power = random.randint(15,20)
            self.agile = random.randint(30,35)
            self.strength = random.randint(15,20)
            self.intelligence = random.randint(0,100-self.agile-self.strength)
            self.wisdom = 100-self.power-self.agile-self.strength-self.intelligence
        elif self.race == '矮人':
            self.power = random.randint(10,15)
            self.agile = random.randint(35,40)
            self.strength = random.randint(10,15)
            self.wisdom = random.randint(15,20)
            self.intelligence = random.randint(0, 100 - self.power - self.agile - self.strength - self.wisdom)
        elif self.race == '元素':
            self.power = random.randint(10,15)
            self.agile = random.randint(15,20)
            self.strength = random.randint(10,15)
            self.intelligence = random.randint(30,35)
            self.wisdom = 100-self.power-self.agile-self.strength-self.intelligence
        self.life = self.strength * 20
        self.magicpoint = (self.intelligence + self.wisdom) * 10
        self.str = "\n力量:" + str(self.power) + "\n敏捷:" + str(self.agile) + "'\n体力:" + str(self.strength) + "\n智力:" + str(self.intelligence) +"\n智慧:" + str(self.wisdom) + "\n生命值:" + str(self.life) +"\n魔法值:" + str(self.magicpoint)
        print('\n','力量:',self.power,'\n','敏捷:',self.agile,'\n','体力:',self.strength,'\n','智力:',self.intelligence,'\n','智慧:',self.wisdom,'\n','生命值:',self.life,'\n','魔法值:',self.magicpoint,'\n')
        return self.str

while True:
    r = Role()
    name = r.setName()
    sex = r.setSex()
    race = r.setRace()
    attribute = r.setAttribute()
    n = int(input("您是否满意目前的角色：0:满意，1:不满意:"))
    if n == 0:
        filename = 'role.txt'
        with open(filename, 'w') as file_object:
            file_object.write("角色姓名:"+name+"\n")
            file_object.write("角色性别:"+sex+"\n")
            file_object.write("角色种族名:"+race+"\n")
            file_object.write("角色属性:" + attribute + "\n")
        break
    elif n == 1:
        print("请重新建立角色")
        continue
    else:
        print("请在0或1之中输入：")
