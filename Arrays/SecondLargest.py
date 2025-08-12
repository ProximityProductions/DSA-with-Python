array = [1,4,3,7,9,2]

def SecondLargest(array):
    Largest,SecondLargest = float('-inf'), float('-inf')    
    for val in array:
        if val>Largest:
            SecondLargest = Largest
            Largest = val
        elif val>SecondLargest and val!=Largest:
            SecondLargest = val
    return SecondLargest
