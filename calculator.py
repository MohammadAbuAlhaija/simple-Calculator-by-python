
num1=float(input("First Number: "))
num2=float(input("Second Number: "))

operation=input("Cloose(+,-,*,/):")

if operation =="+":
    print(f"Result: {num1 + num2}")
elif operation =="-":
    print(f"Result: {num1 - num2}")
elif operation =="*":
    print(f"Result: {num1 * num2}")
elif operation =="/":
    print(f"Result: {num1 / num2}")
else:
    print("Invalid operation")
