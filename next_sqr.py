import math
def next_square(n):
    val = 0
    is_larger = False
    while not is_larger:
        val += 1
        check = val ** 2
        if check < n:
            continue
        else:
            if check == n:
                return int(math.sqrt((val + 1) ** 2))
            else:
                is_larger = True
    return val
        
print(next_square(int(input("Please choose a number. "))))