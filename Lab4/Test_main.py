import unittest
import xmlrunner
from main import add_product_to_queue, get_first_product_from_queue, watch_all_orders_in_queue, clear_orders


class TestOrderQueue(unittest.TestCase):

    def setUp(self) -> None:
        clear_orders()

    def test_add_product_to_queue(self):
        order = add_product_to_queue("Apple", 5)
        self.assertEqual(len(watch_all_orders_in_queue()), 1)
        self.assertEqual(order["product_name"], "Apple")
        self.assertEqual(order["quantity"], 5)

    # Перевірка виключення
    def test_add_product_to_queue_invalid_quantity(self):
        with self.assertRaises(ValueError):
            add_product_to_queue("Banana", -6)

    def test_get_first_product_from_queue(self):
        add_product_to_queue("Orange", 3)
        add_product_to_queue("Lemon", 7)
        order = get_first_product_from_queue()
        self.assertEqual(order["product_name"], "Orange")
        order = get_first_product_from_queue()
        self.assertEqual(order["product_name"], "Lemon")
        self.assertEqual(len(watch_all_orders_in_queue()), 0)

    def test_get_first_product_from_queue_empty(self):
        order = get_first_product_from_queue()
        self.assertEqual(order, {})

    # Перевірка негативного сценарію
    @unittest.expectedFailure
    def test_expected_failure_get_from_empty_queue(self):
        with self.assertRaises(ValueError):
            get_first_product_from_queue()

    def test_get_all_orders_in_queue(self):
        add_product_to_queue("Samsung", 5)
        add_product_to_queue("Casio", 10)
        orders = watch_all_orders_in_queue()

        expected_orders = [
            {"product_name": "Samsung", "quantity": 5},
            {"product_name": "Casio", "quantity": 10}
        ]

        self.assertEqual(orders, expected_orders)

    def test_clear_orders(self):
        add_product_to_queue("Apple", 5)
        result = clear_orders()
        self.assertTrue(result)
        self.assertEqual(len(watch_all_orders_in_queue()), 0)


if __name__ == '__main__':
    with open('Lab4/test-reports.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))
