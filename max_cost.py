'''
Пусть имеется набор предметов, каждый из которых имеет два параметра — вес и ценность.
Также имеется рюкзак определённой вместимости.
Задача заключается в том, чтобы собрать рюкзак с максимальной ценностью предметов
внутри, соблюдая при этом ограничение рюкзака на суммарный вес.
'''

def calc_max_cost(W, obj_arr):
    used_w = 0
    i = 0
    max_cost = 0
    while used_w < W and i < len(obj_arr):
        free_w = W - used_w

        if obj_arr[i][1] <= free_w:
            used_w += obj_arr[i][1]
            max_cost += obj_arr[i][0]
        else:
            used_w += free_w
            max_cost += obj_arr[i][0] * free_w / obj_arr[i][1]

        i = i + 1

    return max_cost

def main():
    n, W = list(map(int, str.split(input())))

    obj_arr = []
    for i in range(n):
        obj_arr.append(str.split(input()))

    obj_arr = [[int(i[0]), int(i[1])] for i in obj_arr]
    obj_arr = sorted(obj_arr, key=lambda l:0 if not l[0] else l[1]/l[0])

    print('%.3f' % calc_max_cost(W, obj_arr))

if __name__ == "__main__":
    main()
