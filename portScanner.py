# We use 'socket' library for connecting

import socket

# 'colorama' is a library for coloring prompts
# If a port is open it will print green and if it is closed in red

from colorama import init, Fore

# Variables for colors

init()

green = Fore.GREEN

reset = Fore.RESET

gray = Fore.LIGHTBLACK_EX

# This function will determine if a port is open

def checkOpenPorts(host, port):

	# Is this 'port' from 'host' open?
	
	# Creates socket
	s = socket.socket()
	
	try:
		# Tries to connect to host using that port
		s.connect((host, port))
		
		# s.settimeout(0.2)	This will add a time for connecting. Makes it faster but can lead to less accuracy
		
	except:
	
		# If it doesnt connect it will return a 'false' statement
		return False
		
	else:
	
		# If connection is established that means it's open ('true')
		return True
		
# Ask the user the host's IP
host = input("Enter host's IP: ")

# Iteration between ports 1 to 1024
for port in range(1, 1024):
	if checkOpenPorts(host, port):
		print(f"{green}[+] {host}:{port} is open	{reset}")
	else:
		print(f"{gray}[!] {host}:{port} is closed	{reset}", end="\r")
