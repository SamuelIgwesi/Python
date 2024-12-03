# name = input("what is your name? ")
# using comma to concatenate

# remove space and capitalize. title() capitalizes all first word letters
# name = name.strip().capitalize()

# destructuring
# first, last = name.split("") /ERROR

# A third parameter can be used called sep="" which means separation... check docs.python.org
# f means format string
# print (f"hello, {name}")

x = float(input("pick a number "))
y = float(input("pick a number "))

z = x / y

# print(f"{z: ,}") # To separate large numbers with comma e.g 1,000
print(f"{z:.2f}") # To specify number of significant figure to round up
