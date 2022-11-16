def tolerance(a,b):
    return abs(a-b) <= 0.000000001

print(tolerance(float(input("Please enter a number. ")), float(input("Please enter another number. "))))