import json

with open("employees.json", "r") as file:
    employees = json.load(file)

new_employee = {
    "Employee ID": 106,
    "Employee Name": "Rohit Mehta",
    "Designation": "Web Developer",
    "Department": "IT",
    "Salary": 58000
}

employees.append(new_employee)

print("-" * 110)
print(f"{'ID':<10}{'Name':<20}{'Designation':<25}{'Department':<20}{'Salary':<15}")
print("-" * 110)

for employee in employees:
    print(
        f"{employee['Employee ID']:<10}"
        f"{employee['Employee Name']:<20}"
        f"{employee['Designation']:<25}"
        f"{employee['Department']:<20}"
        f"${employee['Salary']:<14}"
    )

print("-" * 110)