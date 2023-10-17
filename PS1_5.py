#5.1
#定义划分等式及计算等式的函数
def calculate_expressions(digits, target, current_expr="", current_value=0, index=0,first_digit=True):
    if index == len(digits):
        if current_value == target:
            return [(current_expr, 1)]
        else:
            return []

    solutions = []

    for i in range(index + 1, len(digits) + 1):
        num_str = digits[index:i]
        num = int(num_str)
        
        if first_digit:
            # 对于第一个数字，只能添加正号
            new_expr_plus = num_str
            solutions += calculate_expressions(digits, target, new_expr_plus, num, i, False)
        else:
        # 递归调用：尝试在当前数字后添加正号或负号
            new_expr_plus = current_expr + "+" + num_str
            new_expr_minus = current_expr + "-" + num_str
            solutions += calculate_expressions(digits, target, new_expr_plus, current_value + num, i,first_digit)
            solutions += calculate_expressions(digits, target, new_expr_minus, current_value - num, i,first_digit)

    return solutions

def Find_expressions(target):
    digits="123456789"
    solutions = calculate_expressions(digits, target)
    return solutions

target = 50 #以target=50 举例
expressions = Find_expressions(target)

print(f"打印出所有target={target}的等式")
for expr, _ in expressions:
    print(expr + f"={target}")


#5.2
import matplotlib.pyplot as plt

#计算target=1~100时，solutions的个数
Total_solutions = []
for target in range(1, 101):
    count_solutions = len(Find_expressions(target))
    Total_solutions.append(count_solutions)

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(range(1, 101), Total_solutions, marker='o')
plt.title('Solutions Count for Targets 1 to 100')
plt.xlabel('Target Value')
plt.ylabel('Number of Solutions')
plt.grid(True)

# 找到最大值和最小值及其对应的target
max_solutions = max(Total_solutions)
min_solutions = min(Total_solutions)
max_target = Total_solutions.index(max_solutions) + 1
min_target = Total_solutions.index(min_solutions) + 1

print("Max Solutions:", max_solutions, "for Target:", max_target)
print("Min Solutions:", min_solutions, "for Target:", min_target)

plt.show()

