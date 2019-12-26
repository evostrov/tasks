'''
Бинарный поиск по сортированному по возрастанию списку за O(log n)

На вход получаем две строки:
n a0 a1 a2 .. an
k b0 b1 b2 .. bk

Пример:
5 1 5 8 12 13
5 8 1 23 11 13

Вывод индекс bk в массиве A или -1 если нет такого значения
3 1 -1 -1 5
'''

arr_A = []

def search(l, u, val):
    # Если минимально сужен интервал поиска значит проверяем на рвенство и дальше не идем
    if l==u:
        return l+1 if arr_A[l] == val else -1

    i = int((l + u) / 2)

    if arr_A[i] == val:
        return i+1
    elif arr_A[i] > val:
        # Если еще можем - уменьшаем верхнюю границу поиска или элемент не найден
        return search(l, i-1, val) if i > l else -1
    elif arr_A[i] < val:
        # Если еще можем - увеличиваем нижнюю границу поиска или элемент не найден
        return search(i+1, u, val) if i < u else -1


def main():
    arr_A.extend([ int(x) for x in str.split(input()) ])
    n = int(arr_A.pop(0))

    if n != len(arr_A):
        raise

    arr_B = str.split(input())
    k = int(arr_B.pop(0))

    res = []
    for j in range(0, k):
        res.append(str(search(0, n-1, int(arr_B[j]))))
    print(' '.join(res))


if __name__ == "__main__":
    main()
