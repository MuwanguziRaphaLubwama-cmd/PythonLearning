num1 = float(input("Enter first Number:"))
num2 = float(input("Enter second number:"))
op = input("Enter operation (+,-,*,/):")
if op =="+":
    print(f"Result: {num1 + num2}")
elif op =="-":
    print(f"Result: {num1 - num2}")
elif op =="*":
    print(f"Result: {num1 * num2 }")
elif op == "/":
    print(f"Result: {num1 / num2}")
else:
    print("invalid operation")