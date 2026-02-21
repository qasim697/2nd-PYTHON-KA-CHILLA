import keyword
from typing import List, Dict

"""
variables.py

Concise notes and runnable examples to understand variables in Python.

Run this file to see example outputs:
      python variables.py

Topics covered:
- What is a variable
- Assignment and reassignment
- Dynamic typing
- Multiple assignment / unpacking / swapping
- Naming rules and conventions
- Constants (convention)
- Types, type(), isinstance()
- Mutability vs immutability (brief demo)
- Augmented assignment
- Deleting variables
- Type hints and simple casting
- Useful builtin helpers (id, len)
"""

# ---------------------------
# What is a variable?
# ---------------------------
# A variable is a name bound to an object/value. Python variables are labels
# that reference objects stored in memory. You don't declare types explicitly
# (Python is dynamically typed); you assign values.

# Simple assignment
x = 10           # integer object 10 is bound to name 'x'
print("x =", x, "type:", type(x))

# Reassignment (same name bound to a different object)
x = "hello"      # now 'x' references a str object
print("x reassigned ->", x, "type:", type(x))

# Dynamic typing: variable can hold any type at runtime
x = 3.14
print("x now ->", x, "type:", type(x))

# ---------------------------
# Multiple assignment & unpacking
# ---------------------------
a, b, c = 1, 2, 3    # parallel assignment / tuple unpacking
print("a, b, c =", a, b, c)

# Swap values without a temporary variable
a, b = b, a
print("after swap a, b =", a, b)

# Chain assignment: same object referenced by multiple names
m = n = 0
print("m, n =", m, n)

# ---------------------------
# Naming rules & conventions
# ---------------------------
# - Valid identifiers: start with letter or underscore, followed by letters, digits, or underscores
# - Cannot be a Python keyword (use keyword.iskeyword to check)
print("is 'for' a keyword?", keyword.iskeyword("for"))
# Conventions:
# - lowercase_with_underscores for variables
# - UPPERCASE for constants (convention only, not enforced)

PI = 3.14159   # constant by convention

# ---------------------------
# Types, isinstance(), and type()
# ---------------------------
x = 5
print("type(x) ->", type(x))
print("isinstance(x, int)?", isinstance(x, int))
print("isinstance(x, (int, float))?", isinstance(x, (int, float)))

# Type hints (optional metadata for tools; not enforced at runtime)
name: str = "Alice"
scores: List[int] = [10, 20, 30]
print("name:", name, "scores:", scores)

# ---------------------------
# Casting / Converting types
# ---------------------------
num_str = "42"
num = int(num_str)                # str -> int
flt = float(num)                  # int -> float
s = str(flt)                      # float -> str
print(num_str, "->", num, "->", flt, "->", s)

# Booleans: many objects have truth value (empty containers are False)
print("bool('')", bool(''))
print("bool([1,2])", bool([1,2]))

# ---------------------------
# Mutability vs immutability
# ---------------------------
# Immutable: ints, floats, strings, tuples
# Mutable: lists, dicts, sets
t = (1, 2, 3)
lst = [1, 2, 3]
print("id(t) before:", id(t))
print("id(lst) before:", id(lst))

# Attempting to "change" immutable object creates a new object
t = t + (4,)
print("t after concatenation:", t, "id(t) after:", id(t))

# Mutating a list modifies the same object
lst.append(4)
print("lst after append:", lst, "id(lst) after:", id(lst))

# Be careful when binding multiple names to the same mutable object
a = []
b = a
a.append(1)
print("a:", a, "b (same object):", b)

# ---------------------------
# Augmented assignment
# ---------------------------
c = 5
c += 2   # equivalent to c = c + 2 (for immutable types creates new object)
print("c after += :", c)

# For mutable types, augmented can mutate in-place:
L = [1, 2]
L += [3]   # modifies L in-place (same id)
print("L after += :", L)

# ---------------------------
# Deleting variables
# ---------------------------
temp = "temporary"
print("temp exists:", 'temp' in globals())
del temp
print("temp deleted. Exists now?:", 'temp' in globals())

# ---------------------------
# Useful helpers
# ---------------------------
val = 12345678901234567890
print("id(val):", id(val))
print("Remember: type(), isinstance(), id(), len() are useful tools")

# ---------------------------
# Example: small function using variables
# ---------------------------
def mean(values):
      """Return the arithmetic mean of a non-empty list of numbers."""
      if not values:
            raise ValueError("values must be non-empty")
      total = sum(values)   # local variable 'total'
      count = len(values)   # local variable 'count'
      return total / count  # result is a float

print("mean([1,2,3,4]) =", mean([1, 2, 3, 4]))

# ---------------------------
# End notes
# ---------------------------
# - Variables are simply names bound to objects.
# - Python is dynamically typed: types are associated with objects, not names.
# - Prefer clear, descriptive names and follow PEP8 naming conventions.
# - Use type hints to help linters and readers, but they are optional.
# - Be mindful of mutability when sharing objects across variables.
#
# This file is intended as a short interactive reference. Modify and experiment.
if __name__ == "__main__":
      print("Done running variable examples.")