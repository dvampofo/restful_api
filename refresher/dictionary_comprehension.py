users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longpassword"),
    (3, "usrname", "1234")
]

# Dict comprehension
# storing the entire KV pair
username_mapping = {user[1]: user for user in users}
print(username_mapping["Bob"])

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

# using dict compreh saves me the effort of creating additional for loops
if password_input == password:
    print("Thats the correct password")
else:
    print("Thats the incorrect password")