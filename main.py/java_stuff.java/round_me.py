def tolerance(a,b):
    return abs(a-b) <= 0.01

print(tolerance(float(input("Please enter a number. ")), float(input("Please enter another number. "))))