def narc_number_calc(num):
    return num == sum(int(x) ** len(str(num)) for x in str(num))

print(narc_number_calc(int(input("Plug a value into the narcissistic number calculator! "))))

