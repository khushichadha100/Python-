# Get the name from the user
name = input("Enter a name: ")

# Check if the name is "Taylor"
if name.lower() == "taylor":
    print("Hello, Taylor! Nice to meet you.")
else:
    print("Hello, {}! Welcome!".format(name))

