condition = True
while condition :
    print("1: Addition\t2: Subtraction\t3: Multiplication\t4: Division\n")
    choice = int(input("Enter the choice: "))
    if choice in (1,2,3,4):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            res = num1+num2
            print("The result of addition: ",res)
        elif choice == 2:
            res = num1-num2
            print("The result of subtraction is: ",res)
        elif choice == 3:
            res = num1*num2
            print("The result of multiplication is: ",res)
        elif choice == 4:
            if num1 == 0:
                print("Division not possible")
                break
            elif num1 > 0 :
                res = num1/num2
                print("The result of divison is: ",res)
    else:
        print("Invalid choice!")
    
    cond=input("Would you like to continue? (yes/no): ")
    if cond == 'yes' :
        condition = True
    elif cond == 'no' :
        condition = False   