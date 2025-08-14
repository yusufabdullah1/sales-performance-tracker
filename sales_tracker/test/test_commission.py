# tests/test_commissions.py
import unittest
from sales_tracker.salesperson import SalesPerson
from sales_tracker.sale import Sale
from sales_tracker.commission_calculator import CommissionCalculator

class TestCommissionCalculator(unittest.TestCase):
    def test_commission_tier_1(self):
        sp = SalesPerson("SP001", "Test User", "TestZone")
        sp.add_sale(Sale("2025-01-01", 30000, "Item", 0.8))
        sp.add_sale(Sale("2025-01-02", 30000, "Item", 0.8))
        calc = CommissionCalculator("tiered")
        self.assertAlmostEqual(calc.calculate(sp), 4200.0)  # 60,000 * 0.07

if __name__ == '__main__':
    unittest.main()
