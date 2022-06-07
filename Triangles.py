def check(a, b, c):
    if (a + b < c) or (a + c < b) or (b + c < a):
        print("不是三角形")
        return -1

    a_pow = pow(a, 2)
    b_pow = pow(b, 2)
    c_pow = pow(c, 2)
    tuple = [a_pow,b_pow,c_pow]
    tuple.sort()

    result = tuple[0] + tuple[1] - tuple[2]
    edge = 0
    if tuple[0]==tuple[1]:
        if tuple[0]==tuple[2]:
            edge = 2    # 等边
        else:
            edge = 1    # 等腰
    angle = 0
    if abs(result) <= 0.000001: # 直角
        angle = 0
    elif result > 0.000001:  # 锐角
        angle = 1
    else:  # 钝角
        angle = 2

    if edge == 2:
        print("等边三角形")
        return 0
    if edge == 1:
        if angle == 0:
            print("等腰直角三角形")
            return 1
        elif angle == 1:
            print("等腰锐角三角形")
            return 2
        elif angle == 2:
            print("等腰钝角三角形")
            return 3
    if angle == 0:
        print("直角三角形")
        return 4
    elif angle == 1:
        print("锐角三角形")
        return 5
    elif angle == 2:
        print("直角三角形")
        return 6




# def sort(a, b, c):
#     if a > b and a > c:
#         if b > c:
#             return a, b, c
#         else:
#             return a, c, b
#     if a < b and a < c:
#         if b > c:
#             return b, c, a
#         else:
#             return c, b, a
#     if a < b and a > c:
#         return b, a, c
#     if a > b and a < c:
#         return c, a, b


if __name__ == '__main__':
    print("本程序很蠢，建议输入有理数。")
    print("请输入三角形三条边a,b,c的长度:")
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))
    result = check(a, b, c)
    print("result:",result)
