#定义生成k阶的Pascal_triangle数组的函数
def Pascal_triangle(k):
    triangle=[]
    for i in range(k):
        if i == 0:
           row=[1]
        else:
           row=[1,1]
           if i >= 2:
              for j in range(1,i):
                  row_prev = triangle[i-1]
                  new_number = row_prev[j-1] + row_prev[j]
                  row.insert(j,new_number)
        triangle.append(row)    
    return triangle 

#定义打印Pascal_triangle的函数
def Print_pascals_triangle(triangle):
    max_width = len(' '.join(map(str, triangle[-1])))  # 用于对齐输出
    for row in triangle:
        formatted_row = ' '.join(map(str, row))
        print(formatted_row.center(max_width))

#生成10阶的Pascal_triangle数组
triangle_10=Pascal_triangle(10)
#生成100阶的Pascal_triangle数组
triangle_100=Pascal_triangle(100)
#生成200阶的Pascal_triangle数组
triangle_200=Pascal_triangle(200)

#打印10阶的Pascal_triangle数组
Print_pascals_triangle(triangle_10)

