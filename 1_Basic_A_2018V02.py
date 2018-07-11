# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:45:17 2018

@author: Bing-tsu Chang
"""

# 000 Python 起手式
#-------------------------------------------------------
#: 檢查一下 Python 版本先
import sys 
sys.version

#: 我的第一行程式
print('My first Python code')
print('I come,','I see,','I conquer!')


# 001 變數
#-------------------------------------------------------
a=5
b=a
a=a+1
print(a) #: '=' 是指派一個 '值' 給一個變數的意思
print(b)
a=7
print(b)
#: 變數名稱可以是字母 (大、小寫敏感)、數字或符號，但起始字元必需是英文字母
#: 檢查不能使用的保留字
import keyword
keyword.kwlist


# 002 數字計算
#-------------------------------------------------------
x=a+b #: try '+','-','*','/'

#: 次方
a**2

#: 如何開平方?

#: 特殊運算
a//b
a%b
9^7

#: int() 與 round()
x3=33/a
print(x3)
print(int(x3))
print(round(x3)) #: 四捨五入? try round(2.5)，and round(3.5)


# 003 變數型態
#-------------------------------------------------------
a=8 #: int
b=3.8 #: float
c,d='abc','True' #: str
t,f=True,False #: boolean
print(a,b,c,d,t,f)
type(d)
type(t)


# 003-1 字串運算
#-------------------------------------------------------
s1=c+d
s2=s1*5
print('s1=',s1)
print('s2=',s2)


# 003-2 布林運算
#-------------------------------------------------------
b1=not t
b2=t and f
b3=t or f
print (t,f,b1,b2,b3)

#: 布林值乘以整數 t*3,f*3

#? not, and, or 的運算順序
not f or t and f
((not f) or t) and f 
#-not > and > or-

# 004 Python 內建容器　Container
#-------------------------------------------------------
#-字串 str''
#-列表 list[] # 主要處理數據的工作區
#-數組　tuple()
#-集合　set{value}
#-字典　dict{'key':value} # 建置數據結構的工作區


# 004-1 有序與索引:以 str 字串為例
#-------------------------------------------------------
s1='abcdefgh'
print(s1[3])
#-s1[index]
#-index：start form 0
#-str,list,tuple 均為有序數列, 適用索引 [index]
#-set,dict 為無序數列, 不適用索引
#-反向 index
print(s1[-1],s1[-2])

s1[3:5]


# 005 list 列表 []
#-------------------------------------------------------
Ls=['apple','orange','banana','pear','banana']
Ln=[1,2,2,3,4,5,5,'6','7','7',8,9]
Lb=[True,False]

#? 以加號 '+' 合併: Lc=Ls+Ln+Lb, 會得到什麼
#? 以列表合併: Ld=[Ls,Ln,Lb], 會得到什麼
#? 列表乘以整數 

#? Lc[7] 會得到什麼
#? Ld[2] 會得到什麼
#? Ld 中的布林值 False，要如何索引
Ld=[1,2,3]
Ld*3


# 006 list 編輯
#-------------------------------------------------------

# 006-1 index 查詢 value 的索引位置
Ls.index('banana') 
Ln.index(5,2,6)# (value,start,end)
#: list.command 是 Python 執行內建 method 的基本語法

#-------------------------------------------------------

# 006-2 count 計算 value 的出現次數
#: list.count(value)

#-------------------------------------------------------

# 006-3 取得 list 的長度
#: 好像很容易，來猜猜看?

#-------------------------------------------------------

# 006-4 basic list editing
#: mutability - list is a mutable object
#: 列尾增添 - list.append(new value)
#: 列中插入 - list,insert(index, value)
#: 直接修改 - list[index]='new value'
#: 刪除 - del list[index]
#: task - 將以下列表 Lab 的內容編輯後，成為自 a 至 g 的不重複，連續小寫字母
Lab=['a','B','d','e','e','f']
Lab.append('g')
Lab.insert(2,'c')
Lab[1]='b'
del Lab[4]
print(Lab)

#-------------------------------------------------------

# 006-5 extend
#: extend 與 append　有何不同? 
#: append 將容器視為 _______ 添加於列尾
#: extend 將容器 ________ 添加於列尾


#-------------------------------------------------------

# 006-6 remove 自數列中移除 variable
#: list.remove(value)
#: 如何用　remove 移除指定 index 的元素?

#-------------------------------------------------------

# 006-7 del 與 clear() 移除與清空
Lab.clear()
del Lab

#-------------------------------------------------------

# 006-8 copy() 
#: 複製分 '深複製'、'淺複製'，如果沒有搞清楚，偵錯會很麻煩
#: 如果用 '=' 將舊串列指派給新串列
old_list=[1,2,3]
new_list=old_list
new_list.append('a')
print('new_list',new_list)
print('old_list',old_list)
#: vice versa
#: 子層元素會連動，稱為'深複製'

# 如果用 copy()
old_list=[1,2,3]
new_list=old_list.copy()
new_list.append('a')
print('new_list',new_list)
print('old_list',old_list)
#: 複製後，子層元素不連動

#-------------------------------------------------------

# 006-9 pop() 自列尾（或指定索引）移除並回傳
print(Ln)
a=Ln.pop()
a=Ln.pop(0)
# 這裡因為是函數 pop()的表述，依據其定義，索引不用再加方括號 []

#-------------------------------------------------------

# 006-10 建立空串列備用，別小看這一招，是很多程序的基礎，很常用，很好用！
Le=[]
Le.append(1)

#-------------------------------------------------------


# 007 堆疊 stack 與佇列 Queue
#-------------------------------------------------------
# list 為堆疊結構, 後進先出, append() 與 pop() 均作用於列尾元素
# deque後，變為佇列, 可先進先出, 列尾與列頭均可添加或取出元素
print(Ls)
import collections #: Python 內建模組
Lq=collections.deque(Ls)
#: 'deque' stands for 'double-ended queue'
Lq.append('pineapple') #: 添加元素在列尾
Lq.appendleft ('durian') #: 自列頭添加元素
Lq.popleft() # 自列頭取出最先添加的元素
x=Lq.pop()
#: Queue型態的數列，兩端都可以添加或取出元素


# 008 tuple 數組 ()
#-------------------------------------------------------

# 008-1 tuple 特性
# 不能增, 減, 或執行任何內容編輯
# 元素為有序排列
# 由於不能編輯內容, 所以通常用在計算完以後的儲存容器, 可以避免錯誤
# 在大量迭代 iteration 時, 較 list 省系統資源

#-------------------------------------------------------

# 008-2 建立 tuple
Ts=('apple','orange','banana','pear','banana')
Tn=(1,2,3,4,5,5,6,7,8,9)
Tb=(True,False)
Tc=(Ls,Tn,True,3,'e')

#-------------------------------------------------------

# 008-3 tuple, list, 以及後面要說的 set, 都是指令, 可改變數列的形式
Tuple_s=tuple(Ls) 
List_s=list(Ts)
set_s=set(Ts) #: 元素少了一筆 ?

#-------------------------------------------------------

# 008-4 檢驗元素是否包含在數列中
print(Tuple_s)
print(List_s)
'orange'in Tuple_s
'orange' in List_s
#: 可否檢驗到第二層 ? 
Ld=[Ls,Ln,Lb]
True in Ld
[True, False] in Ld

#-------------------------------------------------------

# 008-5 單一元素 tuple 與字串
Tsingle=('abc',) #: it's a tuple
Ssingle=('abc') # it's a string
# 可以 type() 檢驗

#-------------------------------------------------------


# 009 set 集合 與字典 dict {}
#-------------------------------------------------------

# 009-1 集合
#: 集合中的元素無序，且不可重複
del S5
S5=set() #: 創建空集合
type(S5)
S5.add(1)
L5=[2,3,4,5,6,6,7,8,9,9]
S5.update(L5)
#: unique elements only
S5.add(['a','b','c']) #: ?
S5.add(('a','b','c'))
# try slicing by index: S5[3]
S5[3] #: TypeError，set 無序

#-------------------------------------------------------

# 009-2 創建字典

'''
字典結構
dict={'key 1':value 1,
      'key 2':value 2,
                .....,
      'key n':value n}
'''

S5={
    'obvs':('a','b','c','d','e','f'),
    'x1':(1,2,3,4,5,6)}

S5.update({'x2':(10,20,30,40,50,60)})

S5['x3']=(True,False,False,True,True,True)

#-------------------------------------------------------

# 009-3 集合的邏輯運算
S1={1,2,3,4,5,6,}
S2={4,5,6,7,8,9,}

Su=S1|S2 #union
Si=S1&S2 #intersection
Sd12=S1-S2 #difference
Sd21=S2-S1 #difference
Sun=S1^S2 #unique elements
# 參考講義 P34

#-------------------------------------------------------

# 009-4 字典的應用
#: define 4 variables
var=('name','gender','english','math')

#: 7 observations for each variable
gender=('M','M','M','M','F','M','F')
math=(35,77,69,81,55,47,83)
english=(68,81,60,92,72,33,65)
name=('Georgie','Derek','Dan','Sting','Jade','Anthony','Beth')

#: put the content together
table=(name,gender,english,math)

#: create dict by zip() function
list(zip(var,table))
record=dict(zip(var,table))

# ===========================================================
#: try zip()
m=('a','b','c')
x=(1,2,3,4,5)
y=(5,10,15,20,25)
z=(2,4,6,8,10)

list(zip(m,x,y,z)) #: ?

gp=(x,y,z)
gp_match=list(zip(m,gp)) # basic data structure for a dataframe
# ===========================================================

# 009-5 introduction of DataFrame and Pandas
import pandas as pd
record_df=pd.DataFrame(record) #: create a dataframe
record_df=record_df[['name','gender','english','math']] #: adjust columns

#-------------------------------------------------------

# 009-6 數據匯出 / 入
#: send csv file out
record_df.to_csv("C:/Users/user/Desktop/Ben/test_out_df.csv")
#: try to remove the index

#:read csv file in 
read_df = pd.read_csv("C:/Users/user/Desktop/Ben/test_out_df.csv")
type(read_df)
#-------------------------------------------------------

# 009-7 基本繪圖　matplotlib 套件
import matplotlib.pyplot as plt
plt.scatter(read_df['math'],read_df['english'])
plt.xlabel('math')
plt.ylabel('english')
plt.show()
plt.boxplot([read_df['math'],read_df['english']],
            labels=['math','english'])
plt.show()

#-------------------------------------------------------

# 010 控制結構
#-------------------------------------------------------

# 010-1 邏輯判斷運算元
#: a=b 將 b 的值指派給 a
#: a==b 判斷 a、b 是否相等
#: 還有其他的判斷運算元，請參考 講義 P 26

#-------------------------------------------------------

# 010-2 if 判斷

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

#: 請默寫一次，根據以上語法，自設一個判斷的題目，寫一個 if 判斷

#-------------------------------------------------------
    
# 010-3 for 迴圈
for i in [1,2,3]:
    print('Route:',i) #: 在後面加上 end='', 看看有什麼不同
    print(' Value:',i*2)
    
#: for in in (範圍)，(範圍) 可以是序列元素、可迭代數列、range()

a=[1,2,True]
for i in a:
    print('Route:',i)
    print('Value:',i*2)
#: list 可以，tupple 或 set 可以當(範圍)嗎?
#: 數字可以，文字可以嗎?
#: 布林值可以嗎?
#: 布林值拿去運算，會怎樣?
    
#: 範圍如果用 range() 
#: rantg(n) 表示從 0 到 n-1，共 n 項
#: range()還有哪些可能?
#: 自訂起、止? 調整間隔? 倒數?

for i in range(5):
    print(i)

#-------------------------------------------------------  
    
# 010-4 列表推導式 list comprehension

lc=[i for i in range(10)] #: basic
print(lc)

lca=[a*j for a in ('x','y','z') for j in range(1,4)] #: multiple loop
print(lca)

lcb=[[a*j for a in ('x','y','z')] for j in range(1,4)] #: multiple layer
print(lcb)

#: 練習-請用列表推導式,寫一個包含九九乘法表所有結果的陣列

#-------------------------------------------------------

# 010-5 while 迴圈
#-------------------------------------------------------
x=1 #迴圈外有起始條件的設定
while x<=10: #起始為 True，否則不會執行
    print('Route:',x)
    x=x+1 # 迴圈內一定要有脫離的機制，否則會無限循環
    #縮排表示執行區塊
    #多重迴圈即以縮排來表示迴圈層
print('---------------------')
print('Out of loop:',x)
#-------------------------------------------------------
# 010-6 字串格式 f-string
x=1
while x<=10:
    print(f'Route:{x}')
    x=x+1 
print('---------------------')
print(f'Out of loop:{x}')
#: try different format
print(f' integer:{x:d}\n floating:{x:.2f}\n \
percent:{x:.2%}\n financial(10000 times):{10000*x:,.2f}')

#: 練習-請用 while 迴圈寫一個九九乘法表，並用 f-string 顯示結果

#-------------------------------------------------------

# 010-7 強迫跳過 continue 與強迫脫離 break

#-------------------------------------------------------


# 013 函數基本形式與語法
#-------------------------------------------------------
#: 沒有參數，執行指定動作，沒有傳回值
def f0():
    print ('沒有參數，執行指定動作，沒有傳回值')
f0()

#: 沒有參數，執行指定動作，有傳回值
def f1():
    print('沒有參數，執行指定動作，有傳回值')
    return(3.1416)
f1()  

#: 傳遞參數，參數無預設，執行指定動作，有傳回值
a,b=20,30 # 全局變數
def f2(x,y):
    print ('傳遞參數，參數無預設，執行指定動作，有傳回值')
    a=x+2
    b=y*2
    return(a,b) # 局部變數

f2(3,5)  
print(a,b)

#: 傳遞參數，參數有預設值，執行指定動作，有傳回值
def f3(x,y,z=12):
    print ('傳遞參數，參數有預設值，執行指定動作，有傳回值')
    a=(x+y)/z
    return(a,z)
f3(2,4)
f3(3,5,2)
fn=f3
fv=f3(3,5,2)

#: 這樣會有問題
def f4(x,b=2,y,c=3):
    print ('傳遞參數，預設值參數位置穿插，執行指定動作，有傳回值')
    x=x*b
    y=y+c
    return(x,y)

#: 傳遞參數，預設值參數置後依序排列，執行指定動作，有傳回值
def f4(x,y,b=2,c=3):
    print ('傳遞參數，預設值參數置後依序排列，執行指定動作，有傳回值')
    x=x*b
    y=y+c
    return(x,y,b,c)
f4(5,10)
f4(5,10,4)
f4(5,10,4,8)

#: 參數順序可以自訂
def printme(name,age=35 ):
   print (name,age)
   
printme(age=50,name='John') #: 參數順序可以自訂

#-------------------------------------------------------

# 013-1 遞迴函數

#: fibonacci numbers
#: 費波納契數列 (黃金分割數列) 每數為前兩數加總之數列
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
        #return (fib(n-1)+17)/2

for i in range (10):
    print(f'{fib(i)},',end='') # (...,end='') 作用為何?
   
#: performance issue
#: try fib function with parameters 10, 20, 30, 40
fib(10)

import time
tStart = time.time() #: 計時開始
 
print(fib(10))

tEnd = time.time() #: 計時結束
print (tEnd-tStart)


def fib2(n):
    fib_to=[0,1]
    if n==0:
        return fib_to[0]
    elif n==1:
        return fib_to[1]
    else:
        for i in range(2,n+1):
            fib_to.append(fib_to[i-1]+fib_to[i-2])
        return fib_to[-1]


tStart = time.time() #: 計時開始
 
print(f'{fib2(100):,}')

tEnd = time.time() #: 計時結束
print (tEnd-tStart)



n=int(input('neter your number:'))
tStart = time.time() #: 計時開始
a,b=0,1
if n==0:
    fib=0
elif n==1:
    fib=1
else:
    for i in range(2,n+1):
        a,b=b,a+b
        fib=b

print(fib)

tEnd = time.time() #: 計時結束
print (f'{tEnd-tStart:.8f}')
#-------------------------------------------------------
# -End- of Basic Syntax
# Python 3
#-------------------------------------------------------
  
# 綜合練習 1
#: 最大公約數
Num_1=int(input("請輸入第一個數字："))
Num_2=int(input("請輸入第二個數字："))

#: 依序指派變數
if Num_1<Num_2:
    Tmp_Num=Num_1
    Num_1=Num_2
    Num_2=Tmp_Num
#: 有沒有更簡單的程序?
    
#: 輾轉相除法
while Num_2!=0:
    Tmp_Num=Num_1%Num_2
    Num_1=Num_2
    Num_2=Tmp_Num
    
print("最大公因數=",Num_1) #: 請用 f-string 改寫印出指令

#-------------------------------------------------------  
# 綜合練習 2
#: 樂透號碼產生器

#: 自選號確定下，產生剩餘號碼
import numpy as np # 匯入 numpy

self_s=[3,17]
sn=len(self_s) #: 自選號數目

pool=[i for i in range(1,50)] #: 1-49 母數
for j in self_s:
    pool.remove(j) #: 字母數池中移除自選號

mc_s=[]
for k in range(6-sn):
    s=np.random.randint(len(pool)-k) #: 隨機選取 index
    mc_s.append(pool[s]) #: 取出選取號
    pool.pop(s) #: 移除選取號
    
print(mc_s)

full_set=self_s
full_set.extend(mc_s)
full_set.sort()
print(full_set)

#: 自選號的輸入及防錯流程

self_s=[]
for i in range(1,7):
    try:
        while True:
            x = int(input(f'請輸入第 {i} 組號碼(直接 Enter 即結束輸入):'))
            if x > 49:
                print('數字不能大於49')
            elif x in self_s:
                print(f'重複輸入{x}')
            else:
                break
        self_s.append(x)
    except ValueError:
        break
print(self_s)

# End of Basic Python Syntax ------------------------------