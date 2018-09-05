# this is an atm simulation

print("Welcome to Nano Bank")
print("Insert your Atm card please")
# asking to insert pin
pin = int(input("Enter your Pin: "))

# checking if anything was entered in the pin
if pin > 0:
	print("Pin accepted")
	print("Transactions")
	menu = input("(a)Withdrawal \n(b)Transfer \n(c)Recharge \n(d)Balance Enquiry\n")
	if (menu.lower() == "a"):
		acct_type = input("(a) Savings \n(b) Current \n")
		if (acct_type.lower() == "a" or "b"):
			amount = input("(a)500 \n(b) 1000 \n(c) 20,000 \n(d)Enter other amount")
			if (amount.lower() !="d"):
				print("Take your cash")
			else:
				amnt = float(input("Enter amount:\n"))
				print("take your cash")
				print("Thank you for banking with us!")	
	elif (menu.lower() == "b"):
		rep_acct_no = int(input("Enter recipient account number: "))
		amount_to_be_sent = float(input("Enter the amount to be sent: "))
		confirm = input("Do you want to proceed to send? \n(a) Yes \n(b) No \n")
		if (confirm.lower() == "a"):
			print("Transfer successfull \n Thank you for banking with us")
		else:
			print("Transaction cancelled \n Thank you for banking with us")
	elif (menu.lower() == "c"):
		print("Recharge your phone seamlessly")
		rec_amount = int(input("Enter amount: "))
		phone_number = int(input("Enter phone number: "))
		confam = input("Do you want to proceed to recharge? \n(a) Yes \n(b) No")
		if (confam.lower() == "a"):
			print("Transaction successfull! \n Thank you for banking with us")
		else:
			print("Transaction cancelled")
	elif (menu.lower() == "d"):
		print("This service is currently available")
		print("This software hasn't been connected to our database yet \n Kindly contact your account manager for your account balance and further account details")

else:
	print("You've entered a wrong pin")
