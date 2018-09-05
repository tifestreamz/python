# BMI = Body Mass Index
print("This is a BMI calculator")
print("BMI is an acronym for Body Mass Index")
print("to Calculate your BMI you would have to enter your weight and height")

W = float(input("Please enter your weight in Kg:\n"))
H = float(input("Please enter your height in Metres:\n"))
# BMI formular
BMI = W / (H * H)
print("Your BMI is:", BMI)
if BMI < 18.5:
	print("You are underweight, seek medical attention please")
elif ((BMI >=18.5)and (BMI<25)):
	print("You are Normal")
elif  ((BMI >=25)and (BMI<30)):
	print("You are overweight")
else:
	print("You are obese")
# i've gat to do this range stuff another way round
# and i don"t why this stuff has decided to paint my "and" in red/pink for me
