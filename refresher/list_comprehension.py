# Normal way
numbers = [1,3, 5]
doubled = []

for num in numbers:
    doubled.append(num *2)
print("Normal list: ", doubled)

# List comprehension
doubled2 = [x * 2 for x in numbers]
print("List comprehension: ", doubled2)


# ________________________

friends = ["Rolf", "Sam", "Seoul", "Jen", "songggg"]
starts_s = []

# Normal way
for friend in friends:
    if friend.startswith("S") or friend.startswith("s"):
        starts_s.append(friend)
print("Normal list: ", starts_s)

# List comprehension
starts_s2 = [friend for friend in friends if friend.startswith("S")]
print("List comprehension: ", starts_s2)