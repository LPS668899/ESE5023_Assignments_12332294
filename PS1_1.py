#定义一个按规定要求的排序函数
def  Print_values(a,b,c):
    if a>b:
        if b>c:
            print(a,b,c)
        else:
            if a>c:
               print(a,c,b)
            else:
               print(c,a,b)
    else:
        if b>c:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
        else:
            print(c,b,a)

# Example  
# a=6, b=4, c=3     
Print_values(6,4,3)   
# a=6, b=3, c=4    
Print_values(6,3,4) 
# a=3, b=4, c=6
Print_values(3,4,6)
# a=4, b=3, c=6
Print_values(4,3,6) 
# a=3, b=6, c=4
Print_values(3,6,4) 
# a=4, b=6, c=3
Print_values(4,6,3) 