'''
Реализация кучи на основе полного двоичного дерева
Время выполнения любой операции O(log n)

INPUT:
11
Insert 2
Insert 3
Insert 18
Insert 15
Insert 18
Insert 12
Insert 12
Insert 2
ExtractMax
ExtractMax
ExtractMax

OUTPUT:
18
18
15

'''
max_tree = []

def push_node_down(i):
    fc_ind = 2 * i + 1 if i > 0 else 1
    sc_ind = fc_ind + 1
    if i >= 0 and fc_ind < len(max_tree):
        fc = max_tree[fc_ind]
        sc = max_tree[sc_ind] if sc_ind < len(max_tree) else 0

        if fc > max_tree[i] and fc >= sc:
            t = max_tree[fc_ind]
            max_tree[fc_ind] = max_tree[i]
            max_tree[i] = t
            push_node_down(fc_ind)
        elif sc > max_tree[i]:
            t = max_tree[sc_ind]
            max_tree[sc_ind] = max_tree[i]
            max_tree[i] = t
            push_node_down(sc_ind)


def pop_node_up(i):
    parent_ind = int((i - 1) / 2)
    if i > 0 and i < len(max_tree) and max_tree[i] > max_tree[parent_ind]:
        t = max_tree[parent_ind]
        max_tree[parent_ind] = max_tree[i]
        max_tree[i] = t
        pop_node_up(parent_ind)


def ins_node(node):
    max_tree.append(node)
    pop_node_up(len(max_tree) - 1)


def extract_max_node():
    if len(max_tree) > 1:
        max_node = max_tree[0]
        max_tree[0] = max_tree.pop()
        push_node_down(0)

        return max_node
    else:
        return max_tree.pop()

def main():
    x = int(input())

    cmd = []
    for i in range(x):
        cmd.append(str.split(input()))

    for i in range(len(cmd)):
        if cmd[i][0] == 'ExtractMax':
            print(extract_max_node())
        elif cmd[i][0] == 'Insert':
            ins_node(int(cmd[i][1]))

if __name__ == "__main__":
    main()






