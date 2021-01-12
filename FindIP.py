#Program to To Find Internal IP Address 

import socket

hostname  = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer name : " +hostname)
print("Your Computer IP Address is : "+ IPAddr)
