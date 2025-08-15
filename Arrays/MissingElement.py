array = [1, 2, 4, 5]
n = len(array)

def MissingElement(array):
    expectedSum = n * (n + 1) // 2
    actualSum = sum(array)
    return expectedSum - actualSum

print(MissingElement(array))
