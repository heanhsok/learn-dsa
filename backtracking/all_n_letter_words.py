from typing import List

"""
Given a non-negative integer n, find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.
Iput: 2
Output: ["aa", "ab", "ba", "bb"]
"""


def letter_combination(n):
    def dfs(index, path):
        # stopping condition
        # check if this is the last digit
        if index == n:
            res.append("".join(path))
            return

        for letter in ["a", "b"]:
            path.append(letter)
            dfs(index + 1, path)
            path.pop()

    res = []
    if n > 0:
        dfs(0, [])
    return res


res = letter_combination(2)
print(res)
