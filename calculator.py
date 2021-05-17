#HI THIS IS A CULCULATOR YOU CAN DO ADDITION,SUBTRACTION,MULTIPLICATION,DIVISION.

def main () :
	ai="ANSWER IS"

	a=int(input("ENTER NUMBER   "))

	print()

	b=int(input("ENTER NUMBER   "))

	print()

	#***************************************

	print("1. ADDITION")

	print()

	print("2. SUBTRACTION")

	print()

	print("3. MULTIPLICATION")

	print()

	print("4. DIVISION")

	print()

	print("ENTER 1 , 2 , 3 , 4 ")

	#***********************************

	c=int(input())
	
	#*****************

	print()

	if c==1:
	
		print(ai,a+b)
		
		print()
		
		print("1. BACK TO STARTING")
		
		print()
		
		print("2. EXIT")
		
		print()
		
		bts2=int(input("ENTER 1 , 2  "))
		
		print()
		
		if bts2==1:
			
			main ()
			
		if bts2==2:
			
			print("BYE")
			
			exit()

	#************************	
	
	if c==2:
	
		print(ai,a-b)
		
		print()
		
		print("1. BACK TO STARTING")
		
		print()
		
		print("2. EXIT")
		
		print()
		
		bts2=int(input("ENTER 1 , 2  "))
		
		print()
		
		if bts2==1:
			
			main ()
			
		if bts2==2:
			
			print("BYE")
			
			exit()

	#************************		
	
	if c==3:
	
		print(ai,a*b)
		
		print()
		
		print("1. BACK TO STARTING")
		
		print()
		
		print("2. EXIT")
		
		print()
		
		bts2=int(input("ENTER 1 , 2  "))
		
		print()
		
		if bts2==1:
			
			main ()
			
		if bts2==2:
			
			print("BYE")
			
			exit()
	
	#************************

	if c==4:
	
		print(ai,a/b)
		
		print()
 	
		print("1. BACK TO STARTING")
		
		print()
		
		print("2. EXIT")
		
		print()
		
		bts2=int(input("ENTER 1 , 2  "))
		
		print()
		
		if bts2==1:
			
			main ()
			
		if bts2==2:
			
			print("BYE")
			
			exit()
	
	#************************

	if c>4:
		
		print()
	
		print("YOU DID NOT CHOSE A VALID OPTION")
	
		print()
	
		print("1. BACK TO STARTING")
	
		print()
	
		print("2. EXIT")
	
		print()
	
		bts=int(input("ENTER 1 , 2   "))
	
		print()
		
		if bts==1:
		
			main ()
		
		if bts==2:
		
			print("BYE")
		
			exit()
	
main ()

#******************************************