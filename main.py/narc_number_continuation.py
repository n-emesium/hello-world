def narc_num_calc(num):
    return num == sum(int(x) ** len(str(num)) for x in str(num))

print(narc_num_calc(153))