# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:19:22 2018

@author: User
"""

print ('Hello Martin!')
print ('Hello Martin!', 'How are you?')
a = 3
print (a)
a = 3
a = a + 1
print (a)
a=3
a=a+1
print (a)
#-----------------
a=3
b=4
a=a*b
print (a)
4**0.5
8**(1/3)
(-4)**0.5
a=3
b=3.5
c='abc'
d=True
e='True'
print (a,b,c,d,e)
type (a)
x='abc'
y='deg'
print (x+y)
print (x*3)
t=True
f=False
b=not t
print(not b)
print(t+f)
print(t or f)
print(t and f)
x='abcdef'
x[0]
L=['a','b','c','a']
L2=[0,2,3]
L3=[True,False]
Lc=L+L2+L3
print (Lc)
Ld=[L,L2,L3]
print (Ld)
Lc[3]
Lc.index('b')
Lc.index(False)
Lc.count('a')
Lc[4]
Lc.insert(3,'a')
Lc.append('a')
Lc.extend(L)
Lc.remove(1)
Lc.clear()
del Lc
t=['a','b','c']
t1=t
t.append('d')
print (t)
t1=t.copy()
t.append('e')
print (t)
x=t.pop()
x=t.pop()
x=t.pop(0)
print (x)
t=['a','b','c']
t.sort
t=['a','b','c']
import collections
Lq=collections.deque(t)
Lq.appendleft('test')
Lq.append('test')
Lq.remove('test')
L=list (Lq)
T=tuple(L)
'a' in L
x='a' in L
y='f' in L
t=('s')
s={1,2,3,3,5}
len(s)
# 參考講義 P27
#-------------------------------------------------------

# 012-4 字典 dict，後面實作會用到，是處理複雜數據集的基礎
L1=[1,3,5,7,9]
L2=[2,4,6,8,10]
d1={
    'odd':L1,
    'even':L2
    }
#------------------------------------------------------------------
x=int(input('請輸入成績:'))

if x>100:
    print('Wrong entry,Try again!')
elif x==100:
    print('Perfect!')
elif x>=80:
    print('good!')
elif x>= 60:
    print('Average!')
else:
    print('You need to stydy harder!')
#--------------------------------------------------------------------
a=5
a==6
x=int(input('x:'))
if x>10:
    print("good")
else:
    print("bad")
#----------------------------------------------------------------------
import random

result = 0
for i in range(5):
    x = random.choice([1,2,3,4,5,6])
    result += x
print(result)

import random
x = [1,2,3,4,5,6]
random.shuffle(x)
x = x[2:5]

if 1 in x:
  print('loser')
else:
  print('winner')
#--------------------------------------
for i in {True,'a',3}:
    print('Route:',i)
    print('Value:',i*2) 
for i in [1,2,3]:
    print('Route:',i)
    print('Value:',i*2) 
for i in (1,2,3):
    print('Route:',i)
    print('Value:',i*2)
for i in range(8,2,-1):
    print('Route:',i)
    print('Value:',i*2)
#-----------------------------------------------------------------
#九九乘法表
[i*j for i in range(2,10) for j in range(1,10)]
#------------------------------------------------------------------
# 013-5 while 迴圈
L1=[]
x=1 #迴圈外有起始條件的設定
while x<=10: #起始為 True，否則不會執行
    print('Route:',x)
    L1.append(x)
    x=x+1 # 迴圈內一定要有脫離的機制，否則會無限循環
    #縮排表示執行區塊
    #多重迴圈即以縮排來表示迴圈層
print('---------------------')
print('Sum',sum(L1))
print('Out of loop:',x)
#-------------------------------------------
x=1
while x<=15:
    print('Route:',x)
    x=x+1
print('--------------------------')
print('Sum=',y)
print('Out of loop:',x)
#---------------------------------------------------
import pandas as pd
test_df=pd.DataFrame(d1)
test_df.to_csv("C:/Users/user/Desktop/20180510python lab/test_df.csv")
#--------------------------------------------------------------------
for i in range(2,10):
    for j in range(0,10):
        print(i,'X',j,'=',i*j)
i=2
while i<=9:
    j=1
    while j<=9:
        if j==2:
            continue
        k=i*j
        print('{1}X{2}={0:.2f}'.format(k,i,j))
        j=j+1
    i=i+1
#-------------------------------------------------------------------
Num_1=int(input("第一個數字："))
Num_2=int(input("第二個數字："))
if Num_1<Num_2:
    tmp_num=Num_1
    Num_1=Num_2
    Num_2=tmp_Num
#--------------------------------------------------------
import numpy as np
rnds=[np.random.randint(49) for _ in range(6)]
print(rnds)
lotto_poll=[i for i in range(1,50)]
mc_list=[2,10]
for i in range(len(mc_list)):
    lotto_poll.remove(mc_list[i])
    print(mc_list[i])
    
n_residual=len(lotto_poll)
#----------------------------------------
def plus (n,m):
    return n+m
print (plus(3,5))
#------------------------------------------------------------
x=int(input('Year:'))
y=int(input('Month:'))
z=int(input('Date:'))
if x>=1974:
    print('ok')
else:
    print('ng')
#-------------------------------------------------------------
def sum(a,b,c):
    return a+b+c
value=(1,2,3)
s=sum(*value)
print(s)

def sum(a,b,c):
    return a+b+c
value1={'a':1,'b':2,'c':3}
s=sum(**value1)
print (s)
#---------------------------------------------------------------------
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print(pop_obj)
#------------------------------------------------------------------------
age = int(input('age: '))
if age < 0:
    print('Are you kidding me!')
elif age == 1:
    print('almost human age 14')
elif 1 < age <= 6:
    print('almost human age 20')
else:
    human = 22 + (age*5)
    print('almost human age: ', human)
#-------------------------------------------------------------------------
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 ", site)
else:
    print("没有循环数据!")
print("完成循环!")
#-------------------------------------------------------------------------
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
#-------------------------------------------------------------------------
def paixu(li) :
    max = 0
    for ad in range(len(li) - 1):
        for x in range(len(li) - 1 - ad):
            if li[x] > li[x + 1]:
                max = li[x]
                li[x] = li[x + 1]
                li[x + 1] = max
            else:
                max = li[x + 1]
    print(li)
paixu([41,23344,9353,5554,44,7557,6434,500,2000])
#-------------------------------------------------------------------------
def paixu(li) :
    max = 0
    for ad in range(len(li) - 1):
        for x in range(len(li) - 1 - ad):
            print(x)
paixu([41,23344,9353,5554,44,7557,6434,500,2000])
#-------------------------------------------------------------------------
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
#-------------------------------------------------------------------------
# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total

# 调用sum函数
total=sum( 10, 20 )
print ("函数外 : ", total)
#-------------------------------------------------------------------------
# 计算面积函数
def area(width, height):
    return width * height
area(5,5)
#-------------------------------------------------------------------------
a = 10
def sum ( n ) :
   global a
   n += a
   a = 11
   print ('a = ', a, end = ' , ' )
   print ( 'n = ', n )

sum ( 3 )
print ( '外 a = ', a )
#-------------------------------------------------------------------------
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
 
#多重继承
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
 
test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法
#--------------------------------------------------------------------------
