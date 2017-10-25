import socket

print('Welcome to DNS Lookup')
print('Enter your option 1. URL to IP 2. IP to URL')
op=input('Enter Option')
var=input('Enter URL/IP')
if op==1:
	addr1 = socket.gethostbyname(var)	
	print(addr1)

else:
	addr6 = socket.gethostbyaddr(var)
	print(addr6)
