import tkinter as tk
from tkinter import messagebox
import banking_functions as bf

class BankingAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Elite 102 Banking App")
        self.root.geometry("400x500")
        
        self.current_user_id = None
        self.current_user_name = None

        self.setup_login_screen()

    def clear_screen(self):
        """Removes all widgets from the main window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def setup_login_screen(self):
        """Displays the login screen."""
        self.clear_screen()
        
        tk.Label(self.root, text="Welcome to the Bank", font=("Helvetica", 24)).pack(pady=40)
        
        tk.Label(self.root, text="Email Address:").pack(pady=5)
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.pack(pady=5)
        
        tk.Button(self.root, text="Login", command=self.handle_login, bg="blue", fg="white", font=("Helvetica", 14)).pack(pady=20)
        
        # Test hint
        tk.Label(self.root, text="(Try: shruti@test.example.com)", fg="gray").pack(pady=10)

    def handle_login(self):
        """Logs the user in if the email exists, or creates an account if not."""
        email = self.email_entry.get().strip()
        if not email:
            messagebox.showerror("Error", "Please enter an email address!")
            return
            
        user = bf.get_user_by_email(email)
        if user:
            self.current_user_id = user['id']
            self.current_user_name = user['name']
            self.setup_dashboard()
        else:
            # Quick sign up for demonstration
            self.current_user_id = bf.create_user("New User", email)
            self.current_user_name = "New User"
            messagebox.showinfo("Welcome", "We couldn't find your email, so we created a new account for you!")
            self.setup_dashboard()

    def setup_dashboard(self):
        """Displays the main banking dashboard."""
        self.clear_screen()
        
        tk.Label(self.root, text=f"Welcome, {self.current_user_name}!", font=("Helvetica", 18)).pack(pady=20)
        
        # Balance Display
        self.balance_var = tk.StringVar()
        self.update_balance_display()
        tk.Label(self.root, textvariable=self.balance_var, font=("Helvetica", 32, "bold"), fg="green").pack(pady=10)

        # Deposit Section
        tk.Label(self.root, text="Deposit Amount ($):").pack(pady=(20, 0))
        self.deposit_entry = tk.Entry(self.root)
        self.deposit_entry.pack()
        tk.Button(self.root, text="Make Deposit", command=self.handle_deposit).pack(pady=5)

        # Withdraw Section
        tk.Label(self.root, text="Withdraw Amount ($):").pack(pady=(20, 0))
        self.withdraw_entry = tk.Entry(self.root)
        self.withdraw_entry.pack()
        tk.Button(self.root, text="Make Withdrawal", command=self.handle_withdraw).pack(pady=5)
        
        # Log out
        tk.Button(self.root, text="Log Out", command=self.setup_login_screen, fg="red").pack(pady=30)

    def update_balance_display(self):
        """Fetches the current dynamic balance from the DB."""
        balance = bf.get_balance(self.current_user_id)
        self.balance_var.set(f"${balance:,.2f}")

    def handle_deposit(self):
        try:
            amount = float(self.deposit_entry.get())
            bf.deposit(self.current_user_id, amount)
            self.deposit_entry.delete(0, tk.END)
            self.update_balance_display()
            messagebox.showinfo("Success", f"Successfully deposited ${amount:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def handle_withdraw(self):
        try:
            amount = float(self.withdraw_entry.get())
            bf.withdraw(self.current_user_id, amount)
            self.withdraw_entry.delete(0, tk.END)
            self.update_balance_display()
            messagebox.showinfo("Success", f"Successfully withdrew ${amount:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingAppGUI(root)
    root.mainloop()
