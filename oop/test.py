from enum import Enum
from typing import List, Tuple


class Coin(Enum):
    penny = 1
    nickel = 5
    dime = 10
    quarter = 25


coins = sorted(Coin.__members__.items(), key=lambda x: x[1].value, reverse=True)

balance = 6

out: List[Tuple[int, Coin]] = []
for coin in coins:
    n, balance = divmod(balance, coin[1].value)
    if n:
        out.append((n, coin[1]))
print(out)
