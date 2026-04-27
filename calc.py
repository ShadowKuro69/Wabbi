while True:

    nvm1 = float(input("enter number 1 "))
    nvm2 = float(input("enter number 2 "))
    operation = input("ënter operation (+, -, *, /)")

    if operation == "+":
        print(nvm1 + nvm2)
    elif operation == "-":
        print(nvm1 - nvm2)
    elif operation == "*":
        print(nvm1 * nvm2)
    elif operation == "/":
        print(nvm1 / nvm2)
    else:
        print("invalid operator")

    again = input("again? (y/n): ")
    if again == "n":
            break 


    
