#!/usr/bin/python3
#####error handling exercixe from ACloudGuru python for beginers track.
##### 23/10/2018 JPT
##### 





def calc(num1,num2,op):
	if op =="*":
		return num1*num2
	elif op =="-":
		return num1-num2
	elif op =="+":
		return num1+num2
	elif op =="/":
		return num1/num2
	else:
		return "ERROR"



number1 = int()
number2 = int()
oper = str()
operlist = ["+","-","/","*"]
print("Enter 1st number followed by operator -,+,/ or * followed by 2nd number for calculation")
while True:
	try:
		number1 = int(input("Enter first number: "))
		break
	except ValueError:
		print("That is an invalid entry, please try again.")

while True:
	print("calculating {0} ".format(number1))
	try:
		oper = str(input("Enter the operator -,+,/ or *: "))
		if oper in operlist:
			break
		else:
			print("That is an invalid entry, please try again.")
	except ValueError:
		print("That is an invalid entry, please try again.")

while True:
	print("calculating {0} {1} ".format(number1, oper))
	try:
		number2 = int(input("Enter second number: "))
		break
	except ValueError:
		print("That is an invalid entry, please try again.")

print("calculating {0} {1} {2}".format(number1, oper, number2))


answer=calc(number1,number2,oper)
print("= {0}".format(answer))
	

