import sys

def Hours(mit):
	if mit < 0:
		raise ValueError("You enter a number less than 0")
	else:
		print("{} H, {} M".format(int(mit / 60),mit % 60))

try:
	Hours(int(sys.argv[1]))
except:
	print("Parameter Error")
