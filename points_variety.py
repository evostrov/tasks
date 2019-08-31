'''
Задача о покрытии отрезков точками
Дано N отрезков на прямой. Требуется покрыть их наименьшим числом точек, т.е. найти наименьшее множество точек такое, что каждому отрезку принадлежит хотя бы одна точка.

Следует также заметить, что эту задачу можно рассматривать и как задачу в теории расписаний - требуется покрыть заданный набор мероприятий-отрезков наименьшим числом точек.

Ниже будет описан жадный алгоритм, решающий обе задачи за O (N log N).
'''

def calc_variety(arr):
    res = [arr[0][1]]
    for i in range(0, len(arr)):
        if not(arr[i][0] <= res[-1] and arr[i][1] >= res[-1]):
            res.append(arr[i][1])
    return res

def main():
    n = int(input())
    arr = []
    for i in range(0, n):
        arr.append(str.split(input()))
    arr = [[int(i[0]), int(i[1])] for i in arr]
    arr = sorted(arr, key=lambda l:l[1])
    points_variety = calc_variety(arr)

    print(len(points_variety))
    print(" ".join(list(map(str, points_variety))))

if __name__ == "__main__":
    main()
