def valid_pin(pin):
    return len(pin) in (4,6) and pin.isdigit()

print(valid_pin(input("Please enter a pin to check it's authenticity. ")))