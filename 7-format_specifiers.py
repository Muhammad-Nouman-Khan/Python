#format specifiers = {value : flag} format a value based on what flags are inserted

price1 = 3000.14159
price2 = -9870.6512324141515
price3 = 1200.34

print(f"Price 1 is ${price1:+,.2f}")  # add + for +ve numbers, add comma in price, .2f -> upto 2 decimal
print(f"Price 2 is ${price2:10.2f}")