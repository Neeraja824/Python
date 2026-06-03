#Indexing =  Accessing elements of a sequence using [start : end : step]

credit_number="1234-5678-9012-3456-7890"
print(credit_number[2])
print(credit_number[:7])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-4])
print(credit_number[::2])  #step count
print(credit_number[::-1])

last_digits=credit_number[-4:]
print(f"XXXX-XXXX-XXXX-XXXX-XXXX-{last_digits}")