import unittest
from decimal import Decimal
from tools.unit_economics import contribution


class ContributionTests(unittest.TestCase):
    def test_vat_and_variable_costs(self):
        actual = contribution({"price_incl_vat": "300", "vat_rate": "0.25", "production_ex_vat": "100", "shipping_ex_vat": "40", "payment_fees": "10", "replacement_reserve": "10"})
        self.assertEqual(actual["net_sales_ex_vat"], Decimal("240.00"))
        self.assertEqual(actual["contribution_ex_vat"], Decimal("80.00"))
        self.assertEqual(actual["contribution_margin_pct"], Decimal("33.33"))

    def test_rejects_invalid_money(self):
        with self.assertRaises(ValueError):
            contribution({"price_incl_vat": "NaN", "vat_rate": "0.25"})
        with self.assertRaises(ValueError):
            contribution({"price_incl_vat": "100", "vat_rate": "1.25"})


if __name__ == "__main__":
    unittest.main()
