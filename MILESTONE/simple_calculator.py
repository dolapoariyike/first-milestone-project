def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Division by zero is undefined"
    return num1 / num2

def main():
    print("Welcome to the Simple Calculator")
    
    while True:
        print("\nSelect operation: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter your choice from 1 to 5: ")
        
        if choice == "5":
            print("GoodBye!")
            break
        
        if choice in ["1", "2", "3", "4"]:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
            
            
            if choice == "1":
                result = addition(first_number, second_number)
                print(f"\n{first_number} + {second_number} = {result}")
            elif choice == "2":
                result = subtraction(first_number, second_number)
                print(f"\n{first_number} - {second_number} = {result}")
            elif choice == "3":
                result = multiplication(first_number, second_number)
                print(f"\n{first_number} * {second_number} = {result}")
            elif choice == "4":
                result = division(first_number, second_number)
                print(f"\n{first_number} / {second_number} = {result}")
                
        else:
            print("Invalid Input. Please enter a valid operation")
            
main()