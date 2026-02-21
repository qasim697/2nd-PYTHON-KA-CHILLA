# fruit_basket="Mangoes"
# print(fruit_basket)

# furit_basket=("Mangoes","bananas","grapes")
# print(furit_basket)
# print(furit_basket[0])
# print(furit_basket[1])
# print(type(furit_basket))

# fruit_basket=["Mangoes","bananas","grapes"]
# print(fruit_basket)
# print(fruit_basket[0])
# print(fruit_basket[1])
# print(type(fruit_basket))

# name = input("Enter your name: ")
# print("Hello, " + name + "!")
# aother way input function
# name = input("Enter your name: ") 
# print(f"Hello, {name}!")
# age = int(input("Enter your age: "))
# print(f"You are {age} years old.") 

#coditional logic
# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are a minor.")
# elif age < 65:
#     print("You are an adult.")
# else:
#       print("You are a senior.")
      

# print(4==4) 
# print(4!=4)


# 2) Explicit numeric conversions
print("2) Explicit numeric conversions:")

# int() truncates toward zero (not rounding)
print("int(3.9) ->", int(3.9))
print("int(-3.9) ->", int(-3.9))

# float() converts ints, strings representing numbers
print("float(5) ->", float(5))
print("float('2.5') ->", float("2.5"))

# int() from string with base
print("int('101', 2) ->", int("101", 2))  # binary
print("int('ff', 16) ->", int("ff", 16))  # hex (lowercase allowed)

# complex() accepts numbers or strings that are valid complex literals
print("complex(2, 3) ->", complex(2, 3))
print("complex('1+2j') ->", complex("1+2j"))

# Edge cases: converting NaN/Infinity to int raises ValueError