def add_emp(n, i, s):
    try:
        f = open("employees.txt", "a")
        f.write(n + " | " + i + " | " + s + "\n")
        f.close()
        return True
    except Exception as e:
        print("Error:", e)
        return False

def view_emp():
    try:
        f = open("employees.txt", "r")
        data = f.readlines()
        f.close()
        
        if not data:
            print("No records found.")
            return
            
        print("\n--- Employee Records ---")
        for line in data:
            if line.strip():
                print(line.strip())
                
    except FileNotFoundError:
        print("No file found yet!")

def main():
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        
        ch = input("Choose Option: ")
        
        if ch == '1':
            n = input("Enter Name: ")
            i = input("Enter ID: ")
            s = input("Enter Salary: ")
            
            result = add_emp(n, i, s)
            if result:
                print("Employee Added Successfully")
            
        elif ch == '2':
            view_emp()
            
        elif ch == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()