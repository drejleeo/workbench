import random


def binary_search(target, list, left, right):
    middle = (left + right) // 2
    if left <= right:
        if target == list[middle]:
            return list[middle]
        elif target < list[middle]:
            return binary_search(target, list, left, middle - 1)
        else:
            return binary_search(target, list, middle + 1, right)
    return None


def randomized_bs(target, list, left, right):
    middle = random.randint(left, right)
    if left <= right:
        if target == list[middle]:
            return list[middle]
        elif target < list[middle]:
            return randomized_bs(target, list, left, middle - 1)
        else:
            return  randomized_bs(target, list, middle + 1, right)
    return None


if __name__ == '__main__':
    '''Algorithms can be merged with an optional parameter that determines how the middle is being chosen.'''

    seq = sorted([random.randint(1, 100) for i in range(8)])
    parameters = {
        'target': random.choice(seq),
        'list': seq,
        'left': 0,
        'right': len(seq) - 1,
    }

    alg1 = binary_search(**parameters)
    alg2 = randomized_bs(**parameters)

    print(seq)
    print(f"Targeted {parameters['target']} and found {alg1, alg2}")
