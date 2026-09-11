import socket
#Create a TCP socket

s = socket.socket()
#Optional: set timeout so it doesn't hang
s.settimeout(1)

# Test connection to local host port 80
result = s.connect_ex(("localhost", 80))

#print whether the port is open or closed
print("Port Open" if result == 0 else "Port Closed")

#close the socket
s.close()