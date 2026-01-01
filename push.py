x=39
y=32
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

print("1. Addition :",add(x,y))
print("2. Subtraction :",subtract(x, y))
print("3. Multiplication :",multiply(x, y))
print("4. Division : ",divide(x, y))