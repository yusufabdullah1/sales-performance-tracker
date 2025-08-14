#To generate report
class ReportGenerator:
    def generate(self, salespeople):
        for sp in salespeople:
            print(f"{sp.name} - Total Sales: #{sp.total_sales():,.2f}")
