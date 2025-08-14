#sales amount, date,products and conversion rates
class Sale:
    def __init__(self, date, amount, product, conversion_rate):
        self.date = date
        self.amount = amount
        self.product = product
        self.conversion_rate = conversion_rate
