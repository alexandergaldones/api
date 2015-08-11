import unittest

from .batch_sell_orders import SellOrderCSVParser


class TestSellOrderCSVParser(unittest.TestCase):
    def test_returns_expected_amount_of_parsed_orders(self):
        parser = SellOrderCSVParser('test_file.csv')
        parsed_orders = parser()
        self.assertEqual(len(parsed_orders), 2)

    def test_sell_order_currency_matches_expected_value_for_first_row(self):
        parser = SellOrderCSVParser('test_file.csv')
        expected_value = 'PHP'
        parsed_orders = parser()
        sell_order = parsed_orders[0]
        self.assertEqual(sell_order['currency'], expected_value)

    def test_sell_order_amount_matches_expected_value_for_first_row(self):
        parser = SellOrderCSVParser('test_file.csv')
        expected_value = '100'
        parsed_orders = parser()
        sell_order = parsed_orders[0]
        self.assertEqual(sell_order['amount'], expected_value)

    def test_sell_order_payment_outlet_matches_expected_value_for_first_row(self):
        parser = SellOrderCSVParser('test_file.csv')
        expected_value = 'bpi'
        parsed_orders = parser()
        sell_order = parsed_orders[0]
        self.assertEqual(sell_order['payment_outlet'], expected_value)

    def test_sell_order_pay_with_wallet_matches_expected_value_for_first_row(self):
        parser = SellOrderCSVParser('test_file.csv')
        expected_value = 'PBTC'
        parsed_orders = parser()
        sell_order = parsed_orders[0]
        self.assertEqual(sell_order['pay_with_wallet'], expected_value)

    def test_sell_order_bank_account_name_matches_expected_value_for_first_row(self):
        parser = SellOrderCSVParser('test_file.csv')
        expected_value = 'Test Account'
        parsed_orders = parser()
        sell_order = parsed_orders[0]
        self.assertEqual(sell_order['bank_account_name'], expected_value)

    def test_sell_order_bank_account_number_matches_expected_value_for_first_row(self):
        parser = SellOrderCSVParser('test_file.csv')
        expected_value = '1234567890'
        parsed_orders = parser()
        sell_order = parsed_orders[0]
        self.assertEqual(sell_order['bank_account_number'], expected_value)

    def test_sell_order_currency_matches_expected_value_for_subsequent_row(self):
        parser = SellOrderCSVParser('test_file.csv')
        expected_value = 'PHP'
        parsed_orders = parser()
        sell_order = parsed_orders[1]
        self.assertEqual(sell_order['currency'], expected_value)

    def test_sell_order_amount_matches_expected_value_for_subsequent_row(self):
        parser = SellOrderCSVParser('test_file.csv')
        expected_value = '150'
        parsed_orders = parser()
        sell_order = parsed_orders[1]
        self.assertEqual(sell_order['amount'], expected_value)

    def test_sell_order_payment_outlet_matches_expected_value_for_subsequent_row(self):
        parser = SellOrderCSVParser('test_file.csv')
        expected_value = 'bdo'
        parsed_orders = parser()
        sell_order = parsed_orders[1]
        self.assertEqual(sell_order['payment_outlet'], expected_value)

    def test_sell_order_pay_with_wallet_matches_expected_value_for_subsequent_row(self):
        parser = SellOrderCSVParser('test_file.csv')
        expected_value = 'PBTC'
        parsed_orders = parser()
        sell_order = parsed_orders[1]
        self.assertEqual(sell_order['pay_with_wallet'], expected_value)

    def test_sell_order_bank_account_name_matches_expected_value_for_subsequent_row(self):
        parser = SellOrderCSVParser('test_file.csv')
        expected_value = 'Another Test Account'
        parsed_orders = parser()
        sell_order = parsed_orders[1]
        self.assertEqual(sell_order['bank_account_name'], expected_value)

    def test_sell_order_bank_account_number_matches_expected_value_for_subsequent_row(self):
        parser = SellOrderCSVParser('test_file.csv')
        expected_value = '0987654321'
        parsed_orders = parser()
        sell_order = parsed_orders[1]
        self.assertEqual(sell_order['bank_account_number'], expected_value)
