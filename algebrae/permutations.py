"""draft file - workbench, ideas"""


def permute(list, s):

    if list == 1:
        return s
    else:
        return [
            f'{x} * {y}'
            for x in permute(1, s)
            for y in permute(list - 1, s)
            if eval(f'{x} * {y}') == 72
        ]


def permutation(list, start, end):

    '''This prints all the permutations of a given list
       it takes the list,the starting and ending indices as input'''
    if (start == end):
        print(list)
    else:
        for i in range(start, end + 1):
            list[start], list[i] = list[i], list[start]  # The swapping
            permutation(list, start + 1, end)
            list[start], list[i] = list[i], list[start]  # Backtracking


if __name__ == '__main__':

    # l = [1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72]
    #
    # for el in permute(list=3, s=l):
    #     print(el)

    permutation([1, 2, 3], 0, 2)  # The first index of a list is zero
