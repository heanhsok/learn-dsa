def is_palindrome_str(s):
    return s[::] == s[::-1]


def is_palindrome(s: str) -> bool:
    def recurse(l, r):
        if l >= r:
            return True
        if s[l] != s[r]:
            return False
        return recurse(l + 1, r - 1)

    return recurse(0, len(s) - 1)


def is_palindrome_substr(s: str):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome_substr(s[1:-1])


print(is_palindrome_str("abc"))
print(is_palindrome_str("aba"))

print(is_palindrome("abc"))
print(is_palindrome("aba"))

print(is_palindrome_substr("abc"))
print(is_palindrome_substr("aba"))
