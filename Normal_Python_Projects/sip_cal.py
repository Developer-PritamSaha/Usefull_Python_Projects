from openpyxl import Workbook
from datetime import datetime

def calculate_sip(monthly_investment, annual_return, time_years):
    """Calculate SIP returns with annual compound interest"""
    annual_investment = monthly_investment * 12
    rate = (annual_return / 100)
    total_amount = 0
    yearly_data = []

    for year in range(1, time_years + 1):
        # Add this year's investment
        total_amount += annual_investment
        # Apply compound interest
        total_amount *= (1 + rate)
        
        invested_amount = annual_investment * year
        returns = total_amount - invested_amount
        
        yearly_data.append([
            year,
            invested_amount,
            returns,
            total_amount
        ])
    
    return yearly_data

def save_to_excel(data, filename="sip_calculator_results.xlsx"):
    """Save results to Excel file"""
    wb = Workbook()
    ws = wb.active
    ws.title = "SIP Calculator"

    # Add headers
    headers = ["Year", "Invested Amount", "Returns", "Total Value"]
    ws.append(headers)

    # Add data
    for row in data:
        ws.append([round(val, 2) for val in row])

    wb.save(filename)

def main():
    # Get user inputs
    monthly_sip = float(input("Enter monthly SIP amount: "))
    annual_return = float(input("Enter expected annual return (%): "))
    time_years = int(input("Enter time period (years): "))

    # Calculate SIP returns
    results = calculate_sip(monthly_sip, annual_return, time_years)

    # Save to Excel
    save_to_excel(results)
    print(f"Results saved to sip_calculator_results.xlsx")

if __name__ == "__main__":
    main()