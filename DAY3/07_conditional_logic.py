# Examples and small demos for conditional logic in Python

def comparisons_demo(a, b, c):
    # Comparison operators
    print("comparisons:", a, b, c)
    print("== :", a == b)
    print("!= :", a != b)
    print("<  :", a < b)
    print("<= :", a <= b)
    print(">  :", a > b)
    print(">= :", a >= b)

    # Chained comparisons: evaluates like (a < b) and (b < c)
    # Mathematically: $$a < b < c$$
    print("chained a < b < c:", a < b < c)

def truthy_falsy_demo(values):
    # Truthy / falsy: used when an expression is expected to be boolean
    # Falsy examples: False, None, 0, 0.0, '', [], {}, set()
    for v in values:
        print(repr(v), "->", bool(v))

def if_elif_else_demo(x):
    # Basic branching
    if x < 0:
        print("negative")
    elif x == 0:
        print("zero")
    else:
        print("positive")

def nested_and_shortcircuit_demo(item):
    # Short-circuiting with and/or: right side skipped if not needed
    # This avoids errors when evaluating expressions with side effects.
    if item is not None and "key" in item:
        print("has key:", item["key"])

    # or returns first truthy operand (can be used for defaults)
    name = item.get("name") if item else None
    display = name or "Guest"
    print("display:", display)

def ternary_demo(score):
    # Single-line if (ternary): <true_val> if <cond> else <false_val>
    status = "pass" if score >= 50 else "fail"
    print("score", score, "->", status)

def identity_vs_equality():
    a = [1, 2]
    b = [1, 2]
    c = a
    print("a == b ->", a == b)   # True: equal contents
    print("a is b ->", a is b)   # False: different objects
    print("a is c ->", a is c)   # True: same object

def pattern_matching_demo(value):
    # Python 3.10+: structural pattern matching
    match value:
        case 0:
            print("zero")
        case [x, y]:
            print("list of two:", x, y)
        case {"name": n}:
            print("dict with name:", n)
        case _:
            print("other:", value)

def combined_examples():
    comparisons_demo(1, 2, 3)
    truthy_falsy_demo([0, 1, "", "hi", [], [1], None])
    if_elif_else_demo(-5)
    if_elif_else_demo(0)
    if_elif_else_demo(7)
    nested_and_shortcircuit_demo({"key": "value", "name": "Alice"})
    nested_and_shortcircuit_demo(None)
    ternary_demo(75)
    ternary_demo(40)
    identity_vs_equality()
    pattern_matching_demo([10, 20])
    pattern_matching_demo({"name": "Bob"})
    pattern_matching_demo(42)

if __name__ == "__main__":
    combined_examples()


Key points and '''''''''''gotchas

Basic structure: if, elif, else. elif is a chain of mutually exclusive branches.
Boolean operators: not, and, or. Precedence: 
not
>
and
>
or
not>and>or.
Short-circuiting: and stops if left is falsy; or stops if left is truthy. Useful to avoid errors or provide defaults.
Truthy/falsy: many values coerce to False (0, '', None, empty containers). Use bool(x) to inspect.
Equality vs identity: == checks value equality; is checks object identity (same object).
Membership: in / not in checks items inside sequences/containers.
Chained comparisons: a < b < c is equivalent to (a < b) and (b < c); it's evaluated efficiently.
Ternary: A if cond else B for inline choices.
Pattern matching (match): powerful for structured data (requires Python 3.10+).
Common pitfalls: comparing to None should use is None / is not None, not == None. Beware mutable defaults and side effects in expressions used for branching.
Suggestions

Keep conditionals simple: prefer small functions and early returns (guard clauses) to reduce nesting.
Add unit tests for edge cases (None, empty sequences, boundary values).
Use typing hints for clarity in larger codebases.
If you want, I can:

Put a shorter focused example into the active editor (e.g., guard clauses only), or
Add pytest unit tests that assert behavior for each demo function.'''''''''''