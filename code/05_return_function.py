# 05_return_function.py

# 此示例示意函数为作函数的返回值

def get_fx():
    s = input('请输入您要做的操作: ')
    if s == '求最大':
        return max
    elif s == '求最小':
        return min
    elif s == '求和':
        return sum

L = [2,4,6,8,10]
print(L)
f1 = get_fx()
print(f1(L))
