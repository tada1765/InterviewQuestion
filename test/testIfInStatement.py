print("in" in "input") # True
print("in" in "violet")# False
print("in" in ["in", "out"]) # True
print("in" in ["indigo", "violet"])# False
print("in" in {"in": "out"}) # True
print("in" in {"out": "in"})# False
print("in" in ("in", "out")) # True
print("in" in ("int", "out")) # False
print(1 in (1, (2, (4), (5)), (3, (2, (4)), (4)))) # True
print(4 in (1, (2, (4), (5)), (3, (2, (4)), (4)))) # False
print(2 in (1, (2, (4), (5)), (3, (2, (4)), (4)))) # False
print((2, (4), (5)) in (1, (2, (4), (5)), (3, (2, (4)), (4)))) # True
print((2, (4)) in (1, (2, (4), (5)), (3, (2, (4)), (4)))) # False
print(4 in (2, (4), (5))) # True