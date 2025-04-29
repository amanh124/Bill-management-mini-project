import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="124421",
    database="electric_bill"
)

cursor = db.cursor()

# Calculate bill based on units
def calculate_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return (100 * 5) + (units - 100) * 7
    else:
        return (100 * 5) + (100 * 7) + (units - 200) * 10

# Create - Add new customer bill
def add_bill():
    name = input("Enter customer name: ")
    units = int(input("Enter units consumed: "))
    bill = calculate_bill(units)

    sql = "INSERT INTO bills (customer_name, units, total_bill) VALUES (%s, %s, %s)"
    val = (name, units, bill)
    cursor.execute(sql, val)
    db.commit()

    print(f"✅ Bill added for {name} - ₹{bill}")

# Read - View all bills
def view_bills():
    cursor.execute("SELECT * FROM bills")
    records = cursor.fetchall()

    print("\n--- All Bills ---")
    for r in records:
        print(f"ID: {r[0]}, Name: {r[1]}, Units: {r[2]}, Bill: ₹{r[3]}")

# Update - Update a customer's bill
def update_bill():
    id = int(input("Enter customer ID to update: "))
    new_units = int(input("Enter new units consumed: "))
    new_bill = calculate_bill(new_units)

    sql = "UPDATE bills SET units = %s, total_bill = %s WHERE id = %s"
    val = (new_units, new_bill, id)
    cursor.execute(sql, val)
    db.commit()

    print(f"✅ Bill updated for customer ID {id}")

# Delete - Remove a customer's bill
def delete_bill():
    id = int(input("Enter customer ID to delete: "))

    sql = "DELETE FROM bills WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    db.commit()

    print(f"✅ Customer ID {id} deleted")

# Main program
def main():
    while True:
        print("\n--- Electric Bill Management ---")
        print("1. Add New Bill (Create)")
        print("2. View All Bills (Read)")
        print("3. Update Bill (Update)")
        print("4. Delete Bill (Delete)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_bill()
        elif choice == '2':
            view_bills()
        elif choice == '3':
            update_bill()
        elif choice == '4':
            delete_bill()
        elif choice == '5':
            break
        else:
            print("❌ Invalid choice! Please try again.")

    cursor.close()
    db.close()
    print("Goodbye! 👋")

if __name__ == "__main__":
    main()
