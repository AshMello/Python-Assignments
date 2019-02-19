import unittest
from classesshoppinglist import *

class ShoppingListTests(unittest.TestCase):
    def setUp(self):
        self.shoppinglist = ShoppingList(self)
        print("SETUP")
    
    def total_amount(self):
        print("test_total_amount")
        result = self.shoppinglist.total_amount(5,2)
        self.assertEqual(10, result)

    
    def tearDown(self):
        print("TEARDOWN")

unittest.main()