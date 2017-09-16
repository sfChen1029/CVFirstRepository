import sys
if(sys.argv[1] == "-age"):
	i = sys.argv[2]
	if((int)(i) > 20):
		print("You're old")
	else:
		print("You're not old")
