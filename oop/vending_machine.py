from typing import List, Tuple
from enum import Enum
import unittest


class Coin(Enum):
    """
    An enumeration representing different types of coins with their values.

    Attributes:
        penny (int): Represents a penny with a value of 1.
        nickel (int): Represents a nickel with a value of 5.
        dime (int): Represents a dime with a value of 10.
        quarter (int): Represents a quarter with a value of 25.
    """

    penny = 1
    nickel = 5
    dime = 10
    quarter = 25


class Product:
    """
    Represents a product with a name, price, and quantity.

    Attributes:
        name (str): The name of the product.
        price (int): The price of the product in cents.
        quantity (int): The quantity of the product in stock.

    Methods:
        __str__: Returns a string representation of the product.
    """

    def __init__(self, name: str, price: int):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            price (int): The price of the product in cents.
        """
        self.name = name
        self.price = price
        self.quantity = 0

    def __str__(self):
        """
        Returns a string representation of the product.

        Returns:
            str: A string in the format "name price quantity".
        """
        return f"{self.name} {self.price} {self.quantity}"


class Machine:
    """
    Represents a vending machine.

    Attributes:
        products (dict[Product]): A dictionary to store products with their names as keys.
        balance (int): The current balance in the machine in cents.
        coins (list): A sorted list of Coin enum members.

    Methods:
        new_product: Adds a new product to the machine.
        print_products: Returns a list of product details, sorted by price.
        insert_coin: Inserts a coin, updating the machine's balance.
        purchase: Processes the purchase of a product.
        checkout: Returns the change as a list of tuples of coin counts and types.
        restock: Adds stock to a specified product.
    """

    def __init__(self):
        """
        Initializes a new Machine instance.
        """
        self.products: dict[Product] = dict()
        self.balance = 0
        self.coins = sorted(
            Coin.__members__.items(), key=lambda x: x[1].value, reverse=True
        )

    def new_product(self, name: str, price: int) -> None:
        """
        Adds a new product to the machine.

        Args:
            name (str): The name of the new product.
            price (int): The price of the new product in cents.
        """
        product = Product(name, price)
        self.products[name] = product

    def print_products(self) -> List[str]:
        """
        Generates a list of product details, sorted by price.

        Returns:
            List[str]: A list of strings representing each product, formatted as "name price quantity".
        """
        return [
            str(x[1]) for x in sorted(self.products.items(), key=lambda x: x[1].price)
        ]

    def insert_coin(self, coin: Coin) -> None:
        """
        Inserts a coin into the machine, updating the balance.

        Args:
            coin (Coin): The type of coin inserted.
        """
        self.balance += coin.value

    def purchase(self, name: str) -> bool:
        """
        Processes the purchase of a product.

        Deducts the product's price from the machine's balance and decreases the product's quantity.
        The purchase is only successful if the product exists, is in stock, and the machine has sufficient balance.

        Args:
            name (str): The name of the product to be purchased.

        Returns:
            bool: True if the purchase is successful, False otherwise.
        """
        product = self.products[name]
        if product.price <= self.balance and product.quantity >= 1:
            self.balance -= product.price
            product.quantity -= 1
            return True
        return False

    def checkout(self) -> List[Tuple[int, Coin]]:
        """
        Calculates and returns the change to be given to the customer.

        Change is given in the highest coin denominations possible. The machine's balance is reset to 0.

        Returns:
            List[Tuple[int, Coin]]: A list of tuples where each tuple contains the number of coins of a certain denomination and the coin type.
        """
        balance = self.balance
        self.balance = 0
        out: List[Tuple[int, Coin]] = []
        for coin in self.coins:
            n_coin, balance = divmod(balance, coin[1].value)
            if n_coin:
                out.append((n_coin, coin[1]))
        return out

    def restock(self, name: str, quantity: int) -> None:
        """
        Adds stock to an existing product in the machine.

        If the product does not exist in the machine, no action is taken.

        Args:
            name (str): The name of the product to be restocked.
            quantity (int): The number of units to add to the product's stock.
        """
        if not name in self.products:
            return
        self.products[name].quantity += quantity


class TestMachine(unittest.TestCase):
    def test_new_product(self):
        machine = Machine()
        machine.new_product("Chips", 50)
        machine.restock("Chips", 10)
        machine.new_product("Candy", 25)
        self.assertIn("Candy", machine.products)
        self.assertEqual(machine.products["Candy"].price, 25)

    def test_insert_coin(self):
        machine = Machine()
        machine.new_product("Chips", 50)
        machine.restock("Chips", 10)
        machine.new_product("Candy", 25)
        machine.insert_coin(Coin.quarter)
        self.assertEqual(machine.balance, 25)

    def test_purchase_success(self):
        machine = Machine()
        machine.new_product("Chips", 50)
        machine.restock("Chips", 10)
        machine.new_product("Candy", 25)
        machine.insert_coin(Coin.quarter)
        machine.insert_coin(Coin.quarter)
        success = machine.purchase("Chips")
        self.assertTrue(success)
        self.assertEqual(machine.balance, 0)
        self.assertEqual(machine.products["Chips"].quantity, 9)

    def test_purchase_fail(self):
        machine = Machine()
        machine.new_product("Chips", 50)
        machine.restock("Chips", 10)
        machine.new_product("Candy", 25)
        machine.insert_coin(Coin.penny)
        success = machine.purchase("Chips")
        self.assertFalse(success)
        self.assertEqual(machine.balance, 1)

    def test_checkout(self):
        machine = Machine()
        machine.new_product("Chips", 50)
        machine.restock("Chips", 10)
        machine.new_product("Candy", 25)
        machine.insert_coin(Coin.quarter)
        machine.insert_coin(Coin.dime)
        change = machine.checkout()
        self.assertEqual(change, [(1, Coin.quarter), (1, Coin.dime)])
        self.assertEqual(machine.balance, 0)

    def test_restock(self):
        machine = Machine()
        machine.new_product("Chips", 50)
        machine.restock("Chips", 10)
        machine.restock("Chips", 5)
        self.assertEqual(machine.products["Chips"].quantity, 15)


if __name__ == "__main__":
    unittest.main()
