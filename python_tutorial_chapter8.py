# Loops - python has only For and while loops

# beautiful soup, regex, ML libs: numPy, pandas, seaborn, matplotlib, - django for web dev

# for
for x in "Python":
    print(x)

for x in ['a', 'b', 'c']:
    print(x)

for x in range(5):  # range(2,5) ,,
    print(x)

for x in range(0, 10, 2):
    print(x)

# range is an object
print(type(range(5)))

# For..else -> if for loop completes without immediate break
names = ["abcd", "efgh"]
for name in names:
    if name.startswith("f"):
        print("Found")
        break
else:
    print("Not found")


# While loop

guess = 0
answer = 5

# like for else
while answer != guess:
    answer = int(input("Guess: "))
else:
    pass
