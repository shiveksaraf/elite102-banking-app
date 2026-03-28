import mysql.connector

def main():
    try:
        # Connect to MySQL database
        print("[*] Connecting to the MySQL banking_app database...")
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql123",
            database="banking_app"
        )
        cursor = conn.cursor()
        print("[+] Connection successful!")

        # Create (INSERT)
        print("\n[*] Testing CREATE (INSERT)...")
        cursor.execute("INSERT INTO users (name, email) VALUES ('Shruti Sethi', 'shruti@test.example.com')")
        user_id = cursor.lastrowid
        print(f"[+] INSERT Working: Created user ID {user_id}")
        
        # Read (SELECT)
        print("\n[*] Testing READ (SELECT)...")
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        print(f"[+] SELECT Working: Found user -> {user}")

        # Update (UPDATE)
        print("\n[*] Testing UPDATE...")
        cursor.execute("UPDATE users SET name = 'Shruti S.' WHERE id = %s", (user_id,))
        print("[+] UPDATE Working: Successfully updated name")

        # Delete (DELETE)
        print("\n[*] Testing DELETE...")
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        print(f"[+] DELETE Working: Deleted test user ID {user_id}")
        
        # Verify it's gone
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        if cursor.fetchone() is None:
            print("[+] Verification complete: User no longer exists")

        # Must commit changes
        conn.commit()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("\n[*] Connection gracefully closed.")

if __name__ == "__main__":
    main()
