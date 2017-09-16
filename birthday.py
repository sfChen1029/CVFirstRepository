import sys
if(len(sys.argv) >  1):
	if(sys.argv[1] == "-age"):
		i = sys.argv[2]
		if((int)(i) > 17):
			print("You're old")
		else:
			print("You're not old")
	elif (sys.argv[1] == "-year"):
		i = sys.argv[2]
        	if((int)(i) <2000):
                	print("You're old")
       		else:
                	print("You're not old")
	else:
		print("asdfasfasfadsfas")
