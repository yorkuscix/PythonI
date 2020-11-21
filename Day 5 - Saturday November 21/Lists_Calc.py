# <-- comment - this function takes a list of ints and returns their sum
def add(lst):
    total = 0
    for num in lst:
        total = total + num
    return total

def multiply(lst):
    total = 1
    for num in lst:
        total = total * num
    return total

def subtract(lst):
    total = lst[0]
    for num in lst[1:]:
        total = total - num
    return total

# note that divide will give a float as output
def divide(lst):
    total = lst[0]
    for num in lst[1:]:
        total = total / num
    return total