'''
Сортировка вставкой - наивное решение
Проходим по всем элементам, каждый элемент сравниваем с предыдущим и пока он меньше двигаем его
в сторону начала списка
Время работы не больше чем O(n^2) - так как в худшем случае надо пройти все n элементов
и сдвинуть каждый на n позиций

INPUT:
1 2 5 7 3 6

OUTPUT:
1 2 3 5 6 7
'''

def mv_sort(A):
    for i in range(1, len(A)):
        j = i
        while (j > 0 and A[j] < A[j-1]):
            A.insert(j-1, A.pop(j))
            j -= 1
    return A


def main():
    A = [ int(x) for x in str.split(input()) ]

    print(' '.join([ str(x) for x in mv_sort(A) ]))


if __name__ == "__main__":
    main()
