print("1 -> add")
print("2 -> sub")
print("3 -> mul")
print("4 -> div")

option = int(input("chose an operation: "))

if(option in {1,2,3,4}):
    num1 = int(input("enter 1st num:"))
    num2 = int(input("enter 2nd num:"))

    if (option == 1):
        result = num1 + num2

    elif (option == 2):
        result = num1 * num2
    elif (option == 3):
        result = num1 * num2
    elif (option == 4):
        result = num1 // num2

else:
    print("invalid operation")

print("the result of the operation is {}".format(result))