count = 6
while count > 5:

    print("Calculator")

    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exit")
    
    user_input = int(input("What would you like to do? "))
    if user_input == 1:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        print("Your result:" , int(num1) + int(num2))

    if user_input == 2:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        print("Your result:" , int(num1) - int(num2))

    if user_input == 3:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        print("Your result:" , int(num1) // int(num2))

    if user_input == 4:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        print("Your result:" , int(num1) * int(num2))

    if user_input == 5:
        quit() 