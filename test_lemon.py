import unittest
from lemonade import *


class TestLemonadeStand(unittest.TestCase):

    def test_instance(self):
        object_name = LemonadeStand("New Stand")
        self.assertIsInstance(object_name, LemonadeStand)

    def test_create_stand(self):
        stand1 = LemonadeStand("Test Stand")
        self.assertEqual(stand1.get_stand_name_string() , "Test Stand")

    def test_item(self):
        item1 = MenuItem("Lemonade", 0.5, 1.5)
        self.assertEqual(item1.get_name(), "Lemonade")
        self.assertEqual(item1.get_wholesale_cost(), 0.5)
        self.assertEqual(item1.get_selling_price(), 1.5)
        
    def test_item(self):
        item2 = MenuItem("Lemonade", 0.5, 1.5)
        self.assertEqual(item2.get_name(), "Bad_name_test", "This is going to fail!")

    def test_total_profit(self):
        stand = LemonadeStand('New Stand')
        item1 = MenuItem('Lemonade', 0.5, 1.5)
        stand.add_menu_item(item1)
        item2 = MenuItem('nori', 0.6, 0.8)
        stand.add_menu_item(item2)
        item3 = MenuItem('cookie', 0.2, 1)
        stand.add_menu_item(item3)

        day_0_sales = {
        'lemoNade' : 5,
        'cookie'   : 2
        }
        day_1_sales = {
        'NORI' : 1,
        'Cookie'   : 4
        }

        stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
        stand.enter_sales_for_today(day_1_sales)  # Record the sales for day zero
        self.assertAlmostEqual(stand.total_profit_for_stand(), 10)

if __name__ == '__main__':
    unittest.main()

