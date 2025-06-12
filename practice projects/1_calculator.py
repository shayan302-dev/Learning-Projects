num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Select the operator: /,+,-,*")
if operator =="/":
  print(num1/num2)
elif operator =="+":
  print(num1+num2)
elif operator == '-':
  print(num1-num2)
elif operator =="*":
  print(num1*num2)
else:
  print("Invalid operator")