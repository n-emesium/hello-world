import string
import random
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
nums = [0,1,2,3,4,5,6,7,8,9]
string_options = [alphabet_lower, alphabet_upper, nums]
user_input = input("")

for i in range(len(user_input)):
    string_val = random.choice(string_options)
    if string_val == string_options[0]:
        print(random.choice(alphabet_lower), end = "")
        continue
    elif string_val == string_options[1]:
        print(random.choice(alphabet_upper), end = "")
        continue
    elif string_val == string_options[2]:
        print(random.choice(nums), end = "")
        continue
        
