import math

num = int(input("Enter a number: "))

if num == 0:   # special case (log10(0) is invalid)
    count = 1
else:
    count = int(math.log10(num)) + 1

print("Number of digits:", count)
