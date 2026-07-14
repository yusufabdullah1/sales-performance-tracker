# Sales Performance Tracker and Commission Calculator

## 📌 Overview
A Python-based CLI tool that processes sales transaction data to calculate sales performance metrics, compute commissions using various structures, analyze territories, and generate performance reports.

## 🔧 Features
- Load and process CSV sales data
- Object-oriented design with modular components
- Calculates total sales and commissions
- Supports flexible commission tiers
- Territory-based sales reporting
- Simple CLI interface
- Includes unit tests for commission logic

## 📁 Folder Structure
```
├── main.py
├── salesperson.py
├── sale.py
├── commission_calculator.py
├── report_generator.py
├── data/
│   └── sales_data.csv
├── tests/
│   └── test_commissions.py
├── documentation/
│   ├── overview.txt
│   ├── requirements.txt
│   ├── user_guide.txt
│   └── technical_doc.txt
└── README.md
```

## ▶️ How to Run
1. Place your `sales_data.csv` in the `data/` folder.
2. Open a terminal in the project directory.
3. Run:
   ```bash
   python main.py
   ```
4. Input the path:
   ```bash
   data/sales_data.csv
   ```

## 🧪 Testing
Run unit tests using:
```bash
python -m unittest tests/test_commissions.py
```

## ✅ Requirements
- Python 3.8+
- Standard library only (no external packages)

## 📞 Author
yorabd314@gmail.com
