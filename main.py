from src.database import init_db
from src.data_manager import add_expense, generate_sample_data
from src.analysis import analyze_expenses
from src.report import export_reports

def main():
    init_db()
    print("\n=== Personal Expense Tracker ===")
    print("1. Generate sample data")
    print("2. Add one expense")
    choice = input("Choose 1 or 2: ").strip()
    if choice == "1":
        print(f"Added {generate_sample_data()} sample transactions.")
    elif choice == "2":
        add_expense(input("Date (YYYY-MM-DD): ").strip(),
                    input("Category: ").strip(),
                    float(input("Amount in INR: ")),
                    input("Payment method: ").strip(),
                    input("Description: ").strip())
        print("Expense added.")
    else:
        print("Invalid choice.")
        return
    result = analyze_expenses()
    print(f"Total spending: ₹{result['total_spend']:.2f}")
    print(f"Highest spending category: {result['top_category']}")
    export_reports()
    print("Reports saved in outputs/")

if __name__ == "__main__":
    main()
