'''
Class no longer in scope. Not meant to be inherited for future projects
'''
def calculator(num1, num2):
    '''If loops to handle each method inside function, and to standardize method input'''
    user_input = input("\nAdd Subtract Multiply or Divide?")
    if user_input.lower() == "add":
        output = num1+num2
    elif user_input.lower() =='subtract':
        output = num1-num2
    elif user_input.lower() == 'multiply':
        output = num1*num2
    elif user_input.lower() == "divide":
        output = num1/num2
    return output

def main():
    user_input = input("Input two numbers seperated by a space you would like to perform actions on \n")
    in1, in2 = user_input.strip().split()
    in1, in2 = int(in1), int(in2)
    answer = calculator(in1, in2)
    
    print(f"Your Answer is {answer:.1f}")

if __name__ == "__main__":
    main()

