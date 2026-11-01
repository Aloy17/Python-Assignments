values = [42, 3.14, "42", [1, 2], (1, 2), {"x": 1}, {1, 2}] 

for value in values:    
    print(repr(value), "->", type(value).__name__)