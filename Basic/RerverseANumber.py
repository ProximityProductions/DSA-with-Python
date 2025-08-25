x = int(input("Enter a number: "))

def reverse(self, x):
        return int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)

print(reverse(x))