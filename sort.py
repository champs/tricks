"""
quick sort
"""


def sort(arr):
    less = []
    eq = []
    more = []
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            eq.append(i)
        else:
            more.append(i)

    return sort(less) + eq + sort(more)

if __name__ == '__main__':
    arr = [1, 2, 3, 99, 44, 22, 55]
    print sort(arr)
