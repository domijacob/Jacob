from models import Patient, Hospital
from utils import triage_priority, find_available_hospital

#Data Setup

hospitals = {
    "Korle-Bu": Hospital("Korle-Bu", 2),
    "37 Military": Hospital("37 Military", 3000),
    "Tema General": Hospital("Tema General", 2000),
    "Cape Coast Teaching": Hospital("Cape Coast Teaching", 1500),
    "Komfo Anokye Teaching": Hospital("Komfo Anokye Teaching", 10000),
    "Tamale Teaching": Hospital("Tamale Teaching", 8000),
    "Ho Teaching": Hospital("Ho Teaching", 5000),
    "Sunyani Regional": Hospital("Sunyani Regional", 3000),
    "Effia Nkwanta Regional": Hospital("Effia Nkwanta Regional", 2000),
    "Cape Coast Regional": Hospital("Cape Coast Regional", 1500),
    "Koforidua Regional":Hospital("Koforidua Regional", 1000),
    "Bolgatanga Regional": Hospital("Bolgatanga Regional", 500)
}

def run_system():
    print("--- Emergency Bed Referral System ---")
    
    while True:
        print("\n1. Add Patient")
        print("2. Discharge Patient")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Enter Patient Name: ")
            age = int(input("Enter Age: "))
            severity = int(input("Enter Severity (1-5): "))

            patient = Patient(name, age, severity)
            priority = triage_priority(patient)

            print(f"Triage Result: {priority} PRIORITY")

            target_hospital = find_available_hospital(hospitals)

            if target_hospital:
                if target_hospital.allocate_bed(patient):
                    print(f"SUCCESS: Bed assigned at {target_hospital.name}")
                else:
                    print("CRITICAL: Allocation failed")
            else:
                print("ALERT: NO BEDS AVAILABLE!")

        elif choice == "2":
            hosp_name = input("Enter hospital name: ")

            if hosp_name in hospitals:
                hospitals[hosp_name].discharge_patient()
            else:
                print("Hospital not found")

        elif choice == "3":
            print("Exiting system...")
            break

        else:
            print("Invalid choice")
if __name__ == "__main__":
    run_system()
    #///////////////////////DOMI JACOB/////////////////////////