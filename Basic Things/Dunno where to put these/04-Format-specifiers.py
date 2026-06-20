#Format specifiers : {value:flags} format a value based on what flags are inserted
# :.(number)f --> round to that many decimal places (fixed point)
# :(number)  --> allocate to that many spaces
# :<   --> Left justify
# :>   --> Right justify
# :^   --> Centre allign
# :+   --> Use a plus sign to indicate positive value
# :=   --> Place sign to leftmost position
# :    --> Insert a space before positive number
# :,   --> Comma separator

price1 = 3.1021
price2 = -892.23
price3 = 12.34

print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.3f}")
print(f"Price 3 is ${price3:.2f}")

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")
