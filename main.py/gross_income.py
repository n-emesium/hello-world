def calculate(hours, rate_per_hour):
    gross_income = hours * rate_per_hour
    return gross_income
    
print(calculate(int(input("Enter your hours. ")), int(input("Enter your rate per hour. "))))