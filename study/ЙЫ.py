def partitioning(a, l, r, x):
    while l < r:
        while a[l] < x:
            l += 1
        while a[r] > x:
            r -= 1
        if l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
    return l


def quick_sort_helper(a, l, r):
    if r - l + 1 < 2:
        return
    c = partitioning(a, l, r, a[r])
    quick_sort_helper(a, l, c - 1)
    quick_sort_helper(a, c, r)


def quick_sort(a):
    quick_sort_helper(a, 0, len(a) - 1)


a = [1, 3, 5, 2, 4]

quick_sort(a)

print(a)