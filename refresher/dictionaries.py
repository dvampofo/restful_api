friends_ages = {"Ralph": 24, "Adam": 30, "Anne": 27}
print(friends_ages["Adam"])

# Adding to dictionary
friends_ages["Bob"] = 20
print(friends_ages)
# ---------

# Creating a list of dictionaries
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Jim", "age": 30}, 
    {"name": "Anne", "age": 27}    
]

print(friends[0])
print(friends[2])
print("Name: ", friends[0]["name"])
print("Age: ", friends[0]["age"])

# ----------
# Iterating over a dictionary
print("")
student_attendance = {"Ralph": 80, "Jim": 95, "Anne": 87}
for student in student_attendance:
    print(student)
print("")    
for student in student_attendance:
    print(f"Name: {student}: Attendance amount: {student_attendance[student]}")
    
print("Using .items()")    
for student, attendance in student_attendance.items():
    print(f"Name: {student}: Attendance amount: {attendance}") 
    
# ----------
# Calculating average of the values
student_attendance = {"Ralph": 80, "Jim": 95, "Anne": 87}
attendance_values = student_attendance.values()
print("This is the sum: ", sum(attendance_values) / len(attendance_values))