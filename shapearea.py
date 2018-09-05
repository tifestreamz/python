""" this would be a simple program that would allow the user get a list of shapes they want,
then enter the values to have the area calculated"""
# Asking the user to pick a shape
print("Choose any shape below")
menu = input("pick a shape \n(a) Circle \n(b) Rectangle \n(c) Square \n")
# conditional statement to calculate the area of the shape chosen by the user
if (menu.lower() == "a"):
	# ask user to input the parameters
	r = float(input("Enter the radius: "))
	area = 3.142 * r * r
elif (menu.lower() == "b"):
	# ask user to input the parameters
	l = float(input("Enter the lenght: "))
	b = float(input("Enter the breadth: "))
	area = l * b
elif (menu.lower() == "c"):
	# ask user to enter parameters
	l = float(input("Enter the lenght: "))
	area = l * l 
else:
	print("You've either chosen a wrong option or chosen none at all")
print(area)

