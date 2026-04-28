def triage_priority(patient):
    # Nested If logic to determine urgency
    if patient.severity >= 4:
        if patient.age > 60 or patient.age < 5:
            return "IMMEDIATE"
        else:
            return "URGENT"
    elif patient.severity >= 2:
        return "STABLE"
    else:
        return "NON-URGENT"

def find_available_hospital(hospitals_dict):
    for hospital in hospitals_dict.values():
        if hospital.has_space():
            return hospital
    return None