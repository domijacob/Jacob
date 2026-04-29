# Grading System Program

def grading_system():
    print("--- STUDENT GRADING SYSTEM ---")

    # Students Details
    name = input("Enter students full name: ")
    exam = int(input("Enter exam score: "))
    assessment = int(input("Enter assessment score: "))
    fees = int(input("Enter fees paid (out of 100): "))
    
    total = exam + assessment
    
    #Pass and Fail Check
    exam_status = "Passed" if exam >= 25 else "Failed"
    assessment_status = "Passed" if assessment >= 15 else "Failed"
    
    # Requirement 1: Pass both components
    req1 = exam >= 25 and assessment >= 15
    
    # Requirement 2: Condoned (total = 39 but one component failed)
    req2 = total == 39 and (exam < 25 or assessment < 15)
    
    # Fee condition
    fees_paid = fees == 100
    
    # Final decision
    if (req1 or req2) and fees_paid:
        result = "CERTIFICATE ISSUED"
    elif not req1 and not req2:
        if exam < 25 and assessment < 15:
            result = "FAILED - REPEAT (Failed both components)"
        else:
            result = "FAILED"
    else:
        result = "NO CERTIFICATE (Fees not fully paid)"
    
    if req2:
        print("Status: CONDONED")
    
    print(f"Final Decision: {result}")
    print("----")


# Run the program
grading_system()