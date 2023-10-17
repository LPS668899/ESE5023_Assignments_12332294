#定义达到x值的最短步数的函数 
def Least_moves(x):
    moves = 0
    if x == 1:                   #如果x=1,moves=0
        return moves
    else:
        while x > 1:
           if x % 2 == 0:         #如果x为偶数
                 x = x // 2       # 除以2
           else:
                 x = x - 1        #如果x为奇数，减1
           moves += 1             #每进行1次运算，步长加1
        return moves

import random 
x=random.randint(1,100)   #x为1~100的随机数
moves=Least_moves(x)      #计算到x值的最短步数
print(f"获得 {x} RMB的最少步数：{moves}")  #输出获得x元的最少步数为moves