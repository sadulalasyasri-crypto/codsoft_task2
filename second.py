
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
}
def calculator():
    num1=int(input("Enter the first number: "))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("pick an operation: ")
        num2=int(input("Enter the second number: "))
        calculator_function=operations_dict[op_symbol]
        output=calculator_function(num1,num2)
        print(f"{num1} {op_symbol} {num2} = {output}")

        should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit ").lower()
        if should_continue=='y':
            num1=output
        elif should_continue=='n':
            continue_flag=False
            calculator()
        else:
            continue_flag=False
            print("Stop")
calculator()