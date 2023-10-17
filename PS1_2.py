import random

#2.1
#定义一个可以生成指定行数和列数的随机矩阵的函数
def generate_random_matrix(rows,columns):
     matrix=[]
     for i in range(rows):
         row=[]
         for j in range(columns):
             random_numbers = random.randint(0,50) #生产一个0~50之间随机数
             row.append(random_numbers)
         matrix.append(row)
     return matrix    


#生成一个5行10列的矩阵M1
M1=generate_random_matrix(5,10)
#生成一个10行5列的矩阵M2
M2=generate_random_matrix(10,5)

#打印矩阵M1和M2
print("M1=")
for row in M1:
    print(row)
print("M2=")
for row in M2:
    print(row)   
     
#2.2
#定义矩阵乘法函数
def Matrix_multip(M1,M2):
#先判断矩阵是否可以相乘
    if len(M1) != len(M2[0]):                                                  
        print ("矩阵维度不匹配，无法相乘！")
    else:    
        multip_matrix = [[0 for _ in range(len(M1))] for _ in range(len(M1))]
        for i in range(len(M1)): 
            for j in range(len(M1)):
                for k in range(len(M2)):
                    multip_matrix[i][j] = multip_matrix[i][j]+M1[i][k] * M2[k][j]
        return multip_matrix

#计算并打印M1*M2的结果
result=Matrix_multip(M1,M2)
print("M1*M2=")
for row in result:
     print(row)

