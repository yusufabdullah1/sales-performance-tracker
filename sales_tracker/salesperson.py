#saleperson.py
class SalesPerson:
    def __init__(self, id, name, territory):
        self.id = id
        self.name = name
        self.territory = territory
        self.sales = []

    def add_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        return sum(s.amount for s in self.sales)
