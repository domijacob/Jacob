from tax_system import BusinessOwner,SalariedWorker

class TaxSystem:
    def __init__(self):
        self.taxpayers = []

    def register_taxpayer(self):
        print("\n--- Register New Taxpayer ---")
        tin = input("Enter TIN: ").strip()
        name = input("Enter Name: ").strip()
        try:
            income = float(input("Enter Annual Income: "))
        except ValueError:
            print("Invalid income. Registration failed.")
            return

        print("\nSelect Type:")
        print("1. Business Owner")
        print("2. Salaried Worker")
        choice = input("Enter choice (1/2): ").strip()

        if choice == "1":
            taxpayer = BusinessOwner(tin,name,income)
            print("Business Owner registered successfully.")
        elif choice == "2":
            taxpayer = SalariedWorker(tin,name, income)
            print("Salaried Worker registered successfully.")
        else:
            print("Invalid choice. Registration failed.")
            return

        self.taxpayers.append(taxpayer)

    def generate_bill(self):
        if not self.taxpayers:
            print("No taxpayers registered yet.")
            return
        tin = input("\nEnter TIN to generate bill: ").strip()
        for tp in self.taxpayers:
            if tp.tin == tin:
                details = tp.get_details()
                print("\n=== TAX BILL ===")
                print(f"TIN: {details['TIN']}")
                print(f"Name: {details['Name']}")
                print(f"Income: GH₵{details['Income']:,.2f}")
                print(f"Tax Due: GH₵{details['Tax']:,.2f}")
                print("=====\n")
                return
        print("Taxpayer with this TIN not found.")

    def view_all(self):
        if not self.taxpayers:
            print("No taxpayers registered.")
            return
        print("\n=== ALL TAXPAYERS ===")
        for tp in self.taxpayers:
            details = tp.get_details()
            print(f"TIN: {details['TIN']}, Name: {details['Name']}, Income: GH₵{details['Income']:,.2f}, Tax: GH₵{details['Tax']:,.2f}")
        print("=====================\n")

    def run(self):
        while True:
            print("\n=== GHANA TAX SYSTEM ===")
            print("1. Register Taxpayer")
            print("2. Generate Bill")
            print("3. View All Taxpayers")
            print("4. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.register_taxpayer()
            elif choice == "2":
                self.generate_bill()
            elif choice == "3":
                self.view_all()
            elif choice == "4":
                print("Thank you for using the Tax System.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = TaxSystem()
    system.run()