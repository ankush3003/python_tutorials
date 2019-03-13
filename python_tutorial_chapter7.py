# Logical operators - and|or|not|ternary

name = "abc"
if not name.strip():  # remove whitespaces
    print("name is empty")
else:
    print("name is " + name)


age = 22
if age >= 20 and age <= 65:
    # chaining comparison operator
    # condition can also be written directly as 20 <= age <= 65
    print("Eligible")
else:
    pass

# ternary OP
age = 22
if age >= 20:
    message = "eligible"
else:
    message = "Not eligible"

message = "eligible" if age >= 20 else "Not eligible"
print(message)
