name = input("what is your name? ")
# using comma to concatenate

# remove space and capitalize. title() capitalizes all first word letters
name = name.strip().capitalize()

# destructuring
first, last = name.split("")

# A third parameter can be used called sep="" which means separation... check docs.python.org
# f means format string
print (f"hello, {name}")