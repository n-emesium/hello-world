# my solution: 

try:    
    def solution(num):
        mul_3 = []
        mul_5 = []
        for i in range(num):
            if i % 3 == 0:
                mul_3.append(i)
            elif i % 5 == 0:
                mul_5.append(i)
        mul_3.extend(mul_5)
        return sum(mul_3)
except TypeError:
    pass

# optimal solution

def answer(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

#ya gotta work work work! 