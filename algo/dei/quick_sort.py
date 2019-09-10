import random


def get_pivot(list, method):
    if method == 'first':
        return list[0]
    elif method == 'last':
        return list[-1]
    elif method == 'random':
        return random.choice(list)
    elif method == 'median':
        return list[len(list) // 2]


def quick_sort(list, method='last'):
    if len(list) < 2:
        return list
    pivot = get_pivot(list, method)

    left, right = [], []
    for el in list:
        if el < pivot: left.append(el)
        elif el > pivot: right.append(el)
    equals = [pivot] * (len(list) - len(left) - len(right))

    return [*quick_sort(left), *equals, *quick_sort(right)]


if __name__ == '__main__':
    seq = [random.randint(1, 1000) for i in range(20)]

    result = quick_sort(seq)

    print(f'Initial: {seq}\nFinal: {result}')
