# Personal Expense Tracker with Data Visualization

## IMPORTANT: How to run this project

1. Extract this ZIP.
2. Open the folder `Personal-Expense-Tracker-Visualization` in VS Code.
3. Make sure `app.py`, `main.py`, and `requirements.txt` are directly inside the folder you opened.
4. Open **Terminal -> New Terminal** in VS Code.
5. Copy and run these commands ONE AT A TIME:

```powershell
python --version
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

If PowerShell says scripts are disabled, run this first:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.venv\Scripts\Activate.ps1
```

When Streamlit starts, the browser should open to:
`http://localhost:8501`

## What to click

When the dashboard opens:
1. Click **Generate Sample Data** in the left sidebar.
2. Look at the charts and tables.
3. Add your own expense using **Add Expense**.
4. Click **Export Reports** to create CSV/Excel reports.

## Stop the dashboard

Return to the terminal and press `Ctrl + C`.

## Project features

- Expense and income entry
- SQLite database
- CSV import
- Category spending analysis
- Monthly spending trend
- Payment method analysis
- Daily spending trend
- Budget check
- CSV and Excel report export
- Streamlit dashboard

## CSV columns

For your own CSV, use:

`date,category,amount,payment_method,description`
