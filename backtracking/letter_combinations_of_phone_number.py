from typing import List

"""
Input:
"56"

Output:
["jm","jn","jo","km","kn","ko","lm","ln","lo"]
"""

KEYBOARD = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    def dfs(index, path):
        # stopping condition
        # check if this is the last digit
        if index > len(digits) - 1:
            # report the path
            res.append("".join(path))
            return
        for letter in KEYBOARD[digits[index]]:
            path.append(letter)
            dfs(index + 1, path)
            path.pop()

    res = []
    dfs(0, [])
    return res


res = letter_combinations_of_phone_number("56")
print(res)
