wh=input("What doing(+,-,*,/): ")

a=float(input("Enter first numb: "))
b=float(input("Enter second numb: "))

if wh == "+":
    c = a + b
    print("Result " + str(c) + "!")
elif wh == "-":
    c = a - b
    print("Result " + str(c) + "!")
elif wh == "*":
	c = a * b
	print("Result " + str(c) + "!")
elif wh == "/":
	c = a / b
	print("Result " + str(c) + "!")
else:
	print("Incorrect option!")