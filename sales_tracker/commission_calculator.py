# To calculate the commission
class CommissionCalculator:
    def __init__(self, structure):
        self.structure = structure

    def calculate(self, salesperson):
        total = salesperson.total_sales()
        if total > 100000:
            return total * 0.1
        elif total > 50000:
            return total * 0.07
        else:
            return total * 0.05


