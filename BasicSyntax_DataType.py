# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:45:17 2018

@author: user
"""

# 001 第一行程式
print('My first Python code')
print('come','see','conquer')
#-------------------------------------------------------

# 002 變數: 
a=3
b=5
a=a+b+5
b=7
print(a) # '=' 是指派一個 '值' 給一個變數的意思
c='My first line of Phthon code'
print(c) # 變數也可以是 '字串'
#-------------------------------------------------------

# 003 數字計算
x1=a-b
x2=a*b
x3=a/b
print('x3=',x3)
print('取整數：',int(x3))
print(round(x3))
print(round(x3,3)) # round

print(b)
b**2
b**3

# 開根號
b**0.5
8**(1/3)
#-------------------------------------------------------

# 004 變數型態
a=8 #int
b=3.8 #float
c='abc' #str
d='True' 
t=True # boolean
f=False
print(a,b,c,d,t,f) # d vs. t
#-------------------------------------------------------

# 005 字串運算
s1=c+d
s2=c*2
print(s1)

# 布林運算
b1=not t
b2=t and f
b3=t or f
print (t,f,b1,b2,b3)

# not f or t and f 計算順序如何? 
#與依序 ((not f) or t) and f 運算相同嗎?

# 邏輯運算順序　not>and>or
#-------------------------------------------------------

# 006 Python 數據容器　Container
# 字串 str''
# 串列 list[]
# 數組　tuple()
# 集合　set{value}
# 字典　dict{'key':value}
#-------------------------------------------------------

# 007 字串 str
s1='abcdefgh'
print(s1[3])
# s1[index]
# index：start form 0
s2='123456789'
print(s2[8])
# stt、list'tuple 均為有序數列，適用 [index]；set 和　dict 為無序數列，不適用
#-------------------------------------------------------

# 008 串列 list 組成
Ls=['apple','orange','banana','pear','banana']
Ln=[1,2,3,4,5,5,6,7,8,9]
Lb=[True,False]

# 以 value 合併 Lc_e=Ls+Ln+Lb，會得到什麼?
# 以數列合併 Lc_v=[Ls,Ln,Lb]，會得到什麼?

# Lc_e[7] 會得到什麼?
# Lc_v[2] 會得到什麼?
# 如何從 Lc_v 中取出布林值 False?
#-------------------------------------------------------
# 009 串列編輯
#-------------------------------------------------------

# 009-1 index 查詢 value 的索引位置
Ls.index('banana') # (value,start,end)
# list.command 是 Python 的基本運算語法
#-------------------------------------------------------
# 009-2 count 計算 value 的出現次數
# list.count(value)
#-------------------------------------------------------
# 009-3 取得 list 的長度，好像很容易，來猜猜看?
#-------------------------------------------------------
# 009-4 append　自列尾 (右方）添加資料
# list.append(new value)
#-------------------------------------------------------
# 009-5 insert 自指定索引位置添加資料
# list.insert(index,value)
#-------------------------------------------------------
# 009-6 extend 自列尾添加 ???
# extend 與 append　有何不同? 請自己找答案，找到的請舉手? 
# 謝謝這位同學的分享，請大家鼓掌一下 !
# How about extend a two-layer list?
#-------------------------------------------------------
# 009-7 remove 自數列中移除 variable
# list.remove(value)
# 可否用　index 指定要移除的元素?　可否指定到變數後，再移除變數?
#-------------------------------------------------------
# 009-8 del 與 clear() 移除與清空
#-------------------------------------------------------
# 009-9 copy() 有點詭異，但不知道的話，會犯錯，而且找不到原因
# 如果用 '=' 將舊串列指派給新串列，會發生如下的狀況：
old_list=[1,2,3]
new_list=old_list
new_list.append('a')
print('new_list',new_list)
print('old_list',old_list)
# vice versa
# 好像和單一變數的狀況，不太一樣?

# 如果用 copy()
old_list=[1,2,3]
new_list=old_list.copy()
new_list.append('a')
print('new_list',new_list)
print('old_list',old_list)
# 就脫鉤了
#-------------------------------------------------------
# 009-10 pop() 自列尾（或指定索引）移除並回傳
print(Ln)
a=Ln.pop()
a=Ln.pop(0)
# 這裡因為是函數 pop()的表述，依據其定義，索引不用再加方括號 []
#-------------------------------------------------------
# 009-11 建立空串列備用，別小看這一招，很常用，很好用！
Le=[]
Le.append(1)
#-------------------------------------------------------

# 010 堆疊 stack 與佇列 Queue
# 堆疊 後進先出
# 佇列 先進先出

print(Ls)
import collections
Lq=collections.deque(Ls)
# 'deque' stands for 'double-ended queue'
Lq.append('pineapple') # 添加元素在列尾
Lq.popleft() # 自列頭取出最先添加的元素
# Queue型態的數列，兩端都可以添加或取出元素
#-------------------------------------------------------

# 011 數組 tuple
# tuple 不能增、減、編輯，元素有序
#-------------------------------------------------------

# 011-1 建立 tuple
Ts=('apple','orange','banana','pear','banana')
Tn=(1,2,3,4,5,5,6,7,8,9)
Tb=(True,False)
Tc=(Ls,Tn,True,3,'e')

# 由於不能增、減、編輯，所以通常用在計算完以後的儲存容器，可以避免錯誤。
# 在大量迭代 iteration 時，較 list 省系統資源
#-------------------------------------------------------
# 011-2 tuple、list，以及後面要說的 set，也都是動詞
TLs=tuple(Ls) 
LTs=list(Ts)
#-------------------------------------------------------
# 011-3 檢驗元素是否包含在數列中
print(TLs)
print(LTs)
'orange'in TLs
'orange' in LTs
# 可否檢驗第二層?
#-------------------------------------------------------
# 011-4 單一元素 tuple 與字串
Tsingle=('abc',)
Ssingle=('abc')
# 可以 type() 檢驗
#-------------------------------------------------------

# 012 集合
#-------------------------------------------------------

# 012-1 集合中的元素無序，且不可重複
L5=[2,3,4,5,6,6,7,8,9,9]
T5=tuple(L5)
len(T5)
S5=set(T5)
type(S5)
print(S5)
len(S5)
#-------------------------------------------------------

# 012-2 創建集合與編輯 add、update、remove
S7={1,3,5}
S6=set() # 創建空集合
S6.add(7)
S6.update(S7)
S6.remove(7)
#-------------------------------------------------------

# 012-3 集合的邏輯運算
S1={1,2,3,4,5,6,}
S2={4,5,6,7,8,9,}

Su=S1|S2 #union
Si=S1&S2 #intersection
Sd12=S1-S2 #difference
Sd21=S2-S1 #difference
Sun=S1^S2 #unique elements
# 參考講義 P27
#-------------------------------------------------------

# 012-4 字典 dict，後面實作會用到，是處理複雜數據集的基礎
L1=[1,3,5,7,9]
L2=[2,4,6,8,10]
d1={
    'odd':L1,
    'even':L2
    } 

#-------------------------------------------------------

# 013 控制結構
#-------------------------------------------------------
# 013-1 邏輯判斷運算元
# a=b 將 b 的值指派給 a
# a==b 判斷 a、b 是否相等
# 還有其他的判斷運算元，請參考 講義 P 21
#-------------------------------------------------------

# 013-2 if 判斷

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

# 請默寫一次，根據以上語法，自設一個判斷的題目，寫一個 if 判斷
#-------------------------------------------------------
    
# 013-3 for 迴圈
for i in [1,2,3]:
    print('Route:',i)
    print('Value:',i*2)
    
# for in in (範圍)，(範圍) 可以序列元素、數列、range()

a=[1,2,True]
for i in a:
    print('Route:',i)
    print('Value:',i*2)
# list 可以，tupple 或 set 可以當(範圍)嗎?
# 數字可以，文字可以嗎?
# 布林值可以嗎?
# 布林值拿去運算，會怎樣?
    
# 範圍如果用 range() 
# rantg(n) 表示從 0 到 n-1，共 n 項
# range()還有哪些可能?
# 自訂起、止? 調整間隔? 倒數?

for i in range(5):
    print(i)
#-------------------------------------------------------  
    
# 013-4 列表推導式

vec=[2,3,5,7,11]
Lca=[3*i for i in vec] 


Lcb=[3*i for i in range(5)]


Lcl=[[i,i**2] for i in vec]

[3*i for i in vec if i <=5]

vec1=[111,222,333,]
vec2=[3,4]
[i*j for i in vec1 for j in vec2]

# 練習：請用列表推導式寫一個包含九九乘法表所有結果的陣列

#-------------------------------------------------------

# 013-5 while 迴圈

x=1 #迴圈外有起始條件的設定
while x<=10: #起始為 True，否則不會執行
    print('Route:',x)
    x=x+1 # 迴圈內一定要有脫離的機制，否則會無限循環
    #縮排表示執行區塊
    #多重迴圈即以縮排來表示迴圈層
print('---------------------')
print('Out of loop:',x)
#-------------------------------------------------------
# while迴圈 九九乘法表
x=2
while x<= 9:
y=1
while y <=9:
print(f'{x}x{y}={x*y}')
y=y+1
x=x+1
#---------------------------------------------------------

# 013-6 強迫跳過 continue 與強迫脫離 break
# 實作中再詳細說明

# 014 Read and Write Excel file
#-------------------------------------------------------

# 014-1 read excel file

import pandas as pd
# open the file
df = pd.read_excel('C:/Users/user/Desktop/pcourse.xlsx',\
                          sheetname='工作表7')
# 目錄分隔要用 '/'，不能用反斜線 '\'

import pandas as pd
test_df=pd.DataFrame(d1)

# 輸出時通常會送到 csv 檔，因為不只 excel可以取用
test_df.to_csv("C:/Users/user/Desktop/Ben/test_df.csv")


# -End- of Basic Syntax
# Python 3

    
