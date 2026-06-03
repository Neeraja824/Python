# Format Specifiers = {value : flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number)f = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1=3000.14159
price2=9000.657
price3=4500.789

# . specifier
print(f"dot(.) specifier")
print(f"price 1 is {price1:.2f}")
print(f"price 2 is {price2:.2f}")
print(f"price 3 is {price3:.2f}")

# : specifier
print(f"colon(:) specifier")
print(f"price 1 is {price1:10}")
print(f"price 2 is {price2:10}")
print(f"price 3 is {price3:10}")

# < specifier
print(f"Less than(<) specifier")
print(f"price 1 is {price1:<10}")
print(f"price 2 is {price2:<10}")
print(f"price 3 is {price3:<10}")

# > specifier
print(f"Greater than(>) specifier")
print(f"price 1 is {price1:>10}")
print(f"price 2 is {price2:>10}")
print(f"price 3 is {price3:>10}")

# ^ specifier
print(f"cap(^) specifier")
print(f"price 1 is {price1:^10}")
print(f"price 2 is {price2:^10}")
print(f"price 3 is {price3:^10}")

# + specifier
print(f"plus(+) specifier")
print(f"price 1 is {price1:+10}")
print(f"price 2 is {price2:+10}")
print(f"price 3 is {price3:+10}")

#  specifier
print(f"Empty( ) specifier")
print(f"price 1 is {price1: 10}")
print(f"price 2 is {price2: 10}")
print(f"price 3 is {price3: 10}")

# , specifier
print(f"Comma( ) specifier")
print(f"price 1 is {price1:,}")
print(f"price 2 is {price2:,}")
print(f"price 3 is {price3:,}")