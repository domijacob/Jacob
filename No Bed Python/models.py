class Patient:
    def __init__(self, name,age, condition_severity):
        self.name = name
        self.age = age
        self.severity = condition_severity # Scale 1 - 5 where 5 is considererd to be critical



class Hospital:
    def __init__(self, name, total_beds):
        self.name = name
        self.total_beds = total_beds
        self.occupied_beds = 0


    def has_space(self):
        return self.occupied_beds < self.total_beds
    
    def allocate_bed(self):
        if self.has_space():
            self.occupied_beds += 1
            return True
        return False

    # Discharge function
    def discharge_patient(self):
        if self.patients:
            discharged = self.patients.pop(0)  # remove first patient
            self.occupied_beds -= 1
            print(f"{discharged.name} discharged from {self.name}")
            return True
        else:
            print(f"No patients to discharge in {self.name}")
            return False