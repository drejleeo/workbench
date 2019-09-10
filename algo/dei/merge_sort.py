import random


def merge_sort(list):
    if len(list) < 2:
        return list

    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == '__main__':
    seq = [random.randint(1, 100) for i in range(9)]
    result = merge_sort(list=seq)
    print(f'Initial: {seq}\nFinal: {result}')
