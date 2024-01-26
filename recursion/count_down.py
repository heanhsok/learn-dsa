def count_down(n):
    print(n, end=" ")
    if n == 0:
        return
    return count_down(n - 1)


count_down(5)
