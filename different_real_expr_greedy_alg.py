'''
Разложить n на максимальное число различных натуральных чисел
'''

def calc_real_expr(n):
    i = n if n == 1 or n == 2 else 1
    res = []
    rest = n - i
    while rest > i:
        res.append(i)
        i += 1
        rest -= i

    res.append(rest+i)

    return res

def main():
    n = int(input())

    res = calc_real_expr(n)
    print(len(res))
    print(" ".join(list(map(str, res))))

if __name__ == "__main__":
    main()
