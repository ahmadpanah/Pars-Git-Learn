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

elif choice == "b" or choice == "B":
    print ("Substract")
    a = int(input("input First Number: "))
    b = int(input("input Second Number: "))
    sub(a,b)

elif choice == "c" or choice == "C":
    print ("Multiply")
    a = int(input("input First Number: "))
    b = int(input("input Second Number: "))
    mul(a,b)

elif choice == "d" or choice == "D":
    print ("Division")
    a = int(input("input First Number: "))
    b = int(input("input Second Number: "))
    div(a,b)

elif choice == "e" or choice == "E":
    print ("Good Bye!")
    quit()