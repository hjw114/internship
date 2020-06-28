class Product():#产品类
    def __init__(self,price,index,number,name):#传入参数
        self.price=price
        self.index=index
        self.number=number
        self.name=name
    def __str__(self):#打印对象
        return 'name:%s,price:%s,numde:%s,index:%s' % (self.name, self.price, self.number, self.index)
class Stock(object):#库存类
    def __init__(self):
        self.goods = []
    def add(self, product):#添加产品
        if len(self.goods) > 0:
            flag = 0
            for i in range(len(self.goods)):
                if (self.goods[i].index == product.index):
                    self.goods[i].number += product.number
                    flag = 1
                    break
                if (flag != 0):
                    self.goods.append(product)
        else:
            self.goods.append(product)
    def List_all(self):#列出产品
        n = 0
        c = 0
        for i in range(len(self.goods)):
            n += self.goods[i].number
            c += self.goods[i].number * self.goods[i].price
            print('产品ID：%s 产品名称：%s 产品数量：%s 产品价格：%s' % (
            self.goods[i].index, self.goods[i].name, self.goods[i].number, self.goods[i].price))
        print('总计：产品总数：%s 产品总价：%s' % (n, c))


#测试代码
a=Stock()
b=Product(10,123456,100,"apple")
a.add(b)
a.List_all()