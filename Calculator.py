def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

print("A. Additon")
print("B. Substraction")
print("C. Multiply")
print("D. Division")
print("E. Exit")

choice = input("Please Type Your Option: ")

if choice == "a" or choice == "A":
    print ("Additon")
    a = int(input("input First Number: "))
    b = int(input("input Second Number: "))
    add(a,b)