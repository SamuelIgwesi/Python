name = 'sam'
sentence = '%s going home with %s at %dpm'

# PLACE HOLDERS (%s, %d)
# print(sentence % ('Daniel', 'Mary', 4))

# Using f string placeholder format
# print(f"I like {sentence}")

# SLICING: first character is included, end character is excluded
# print(sentence[0:4])

#1. Write a script that adds 15 and 30 and divides the sum by 2. Print out the answer.
# x = 15
# y = 30
# print((x+y)/2)

# 2. Initialize two variables and use arithmetic operators to add, subtract, multiply, divide, and find the remainder.
a = 10
b = 5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

# 4. Create three variables in one line and assign each one a different food item.
x,y,z = ('boy','girl','ant')
# print(x)

# 5. Print out "Hello" ten times using arithmetic operators.
# print('hello' * 10)

# slicing
name = 'Samuel'
# print(name[0:])

# working with lists
shopping_list = ['banana', 'oranges', 'pineapple']
# print(shopping_list[0:2])

shopping_list.append('mango') #Add to a list
# print(shopping_list)

shopping_list[1] = 'pears'
# print(shopping_list) # modify a list

del shopping_list[2] #delete
# print(shopping_list)

# Length of a list
# print(len(shopping_list))


# ARITHMETIC OPERATIONS WITH LISTS
# shopping_list2 = ['rice', 'beans']
# print(shopping_list + shopping_list2)
#
# print(shopping_list2 * 2)

# Maximum and minimum values in a list
# ages = [18,21,19,32]
# print(max(ages))
# print(min(ages))

# DICTIONARIES
# N.B: Keys must be unique and case sensitive and are mutable
student_ages = {'dan': 14, 'ella': 21, 'jake': 17}
student_ages['ella'] = 12
# print(student_ages)
# print(student_ages['jake'])

# TUPLES: Are like other data structures in python but are immutable
# They can be concatenated to create new tuples
tuple = ('boy','girl', 'man')
# print(tuple[1])


# CONDITIONAL STATEMENT
age = 19
# if age < 13:
#     print('A child')
# elif age >= 13 and age < 18:
#     print('A teenager')
# else:
#     print('Adult')

# FOR LOOPS
# num = [1,2,3,4,5,6,4,53,22]
# for i in num:
    # print(i)

# for i in range(0, 20, 2):
#     for j in range(1,3):
#         print(i * j)

# WHILE LOOP
# break terminates the rest of the code once condition is met while continue terminates
# the condition and continues and pass is a do nothing command, acts as a placeholder.
c = 0
while c < 10:
    c = c + 1
    if c == 3:
        continue
    if c == 8:
        break
        pass
    print(c)