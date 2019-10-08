'''
Кодирование Хаффмана - O(n logn) - так как реализация на основе кучи с полным бинарным деревом
'''

from heapq import heappush, heappop

def encode(string):
    letter_count = {}
    for letter in string:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    code = {}
    heap = []
    code_tree = ''
    if len(letter_count.keys()) > 1:
        for k in sorted(letter_count, key=letter_count.get, reverse=True):
            heappush(heap, (letter_count[k], k))
    else:
        code[list(letter_count.keys())[0]] = '0'

    while heap:
        i1 = heappop(heap)
        i2 = heappop(heap)

        new_node = ( i1[0] + i2[0], i1[1] + i2[1] )

        if len(i1[1]) == 1:
            code[i1[1]] = '0'
        else:
            for l in i1[1]:
                code[l] = '0' + code[l]

        if len(i2[1]) == 1:
            code[i2[1]] = '1'
        else:
            for l in i2[1]:
                code[l] = '1' + code[l]

        if heap: heappush(heap, new_node)

    encoded_string = ''
    for letter in string:
        encoded_string += code[letter]

    return list(code.keys()), code, encoded_string

def main():
    string = str(input()).lower()

    letters, code, encoded_string = encode(string)
    print(len(letters), len(encoded_string))

    for k in code.keys():
        print(k + ':', code[k])

    print(encoded_string)

if __name__ == "__main__":
    main()
