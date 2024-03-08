student_attendance = {"Ralph": 80, "Jim": 95, "Anne": 87}

print(list(student_attendance.items()))

# for student, attendance in student_attendance.items():
#     print(f"Name: {student}: Attendance amount: {attendance}") 

# ----------

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

# Easy to read
for name, age, profession in people:
    print(f"Name: {name}, age: {age}, profession: {profession}")

# Not easy to read. Dont know whats happening
for person in people:
    print(f"Name: {person[0]}, age: {person[1]}, profession: {person[2]}")

head, *tail = [1,2,3,4,5]
print(head)
print(tail)

*head2, tail2 = [1,2,3,4,5]
print(head2)
print(tail2)