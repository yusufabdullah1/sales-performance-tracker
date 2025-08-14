#main script to run the Sales Performance Tracker and Commission calculator
from salesperson import SalesPerson
from sale import Sale
from commission_calculator import CommissionCalculator
from report_generator import ReportGenerator
import csv


def load_sales_data(file_path):
    salespeople = {}
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                sp_id = row['SalesPersonID']
                if sp_id not in salespeople:
                    salespeople[sp_id] = SalesPerson(sp_id, row['Name'], row['Territory'])
                sale = Sale(row['Date'], float(row['Amount']), row['Product'], float(row['ConversionRate']))
                salespeople[sp_id].add_sale(sale)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")
    return list(salespeople.values())


def main():
    file_path = input("Enter path to sales data CSV file: ")
    salespeople = load_sales_data(file_path)

    calculator = CommissionCalculator("tiered")
    report = ReportGenerator()

    for sp in salespeople:
        commission = calculator.calculate(sp)
        print(f"{sp.name} earned a commission of #{commission:.2f}")

    report.generate(salespeople)


if __name__ == "__main__":
    main()