# Elite 102 Banking App 🏦

This is my final project for the Code2College Elite 102 course! It is a fully functional, local desktop application that simulates a robust banking system.

## 🌟 Key Features
* User Identity Management: Users can quickly log in or safely create an account.
* Live Database Integration: Deposits and withdrawals dynamically update the account balance instantly.
* Desktop GUI: The entire interaction flows through a clean graphical user interface, rather than a boring terminal.

## 💻 Tech Stack Used
* **Python 3:** The core logic powering transactions.
* **MySQL Database:** Local persistence simulating a real-world banking backend holding `users` and `transactions` tables utilizing `FOREIGN KEY` relationships.
* **Tkinter:** The Python-native GUI library used to build the interactive desktop windows and popups.
* **Unittest:** Python's built-in testing framework to ensure mathematically flawless deposits and prevent overdrafting.

## 🚀 How to Run It

1. First, make sure you have the required Python MySQL connector installed:
   ```bash
   pip install mysql-connector-python
   ```

2. Make sure your local MySQL instance is running and your database is configured with the `schema.sql` template!

3. Run the graphical interface:
   ```bash
   python3 ui.py
   ```

## 🧪 How to Run Automated Unit Tests

I built an automated suite of tests (`test_banking.py`) to mathematically prove my core logic catches bugs. You can execute them by running:
```bash
python3 -m unittest test_banking.py
```
You should see 4 successful test executions guaranteeing that deposits work and overdrafts are blocked!
