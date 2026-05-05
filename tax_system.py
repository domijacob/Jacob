class TaxPayer:
    def __init__(self, tin, name, income):
        self.tin = tin
        self.name = name
        self.income = income

    def calculate_tax(self):
        return 0

    def get_details(self):
        return {
            "TIN": self.tin,
            "Name": self.name,
            "Income": self.income,
            "Tax": self.calculate_tax()
        }
class BusinessOwner(TaxPayer):
     def calculate_tax(self):
        if self.income <= 50000:
            return self.income * 0.15
        elif self.income <= 150000:
            return self.income * 0.20
        else:
            return self.income * 0.25

class SalariedWorker(TaxPayer):
    def calculate_tax(self):
        if self.income <= 30000:
            return self.income * 0.05
        elif self.income <= 70000:
            return self.income * 0.10
        else:
            return self.income * 0.175