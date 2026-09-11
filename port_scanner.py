#Write a program to Check ports 80, 443 on a host (e.g., "localhost")
#use socket to test connection
import socket

host = "localhost"
ports = [80, 443]

for port in ports:
    try:
        user_input = input("enter ports: ")
        port = int(user_input)
        print("you entered:", port)
        break
    except ValueError:
        print("Invalid input. Please enter a port.")

s = socket.socket()

#optional: set timeout so it doesn't hang
s.settimeout(1)
result = s.connect_ex((host,port))

#print whether the port is open or closed
print("Port open" if result ==0 else "Port Closed")

#close the socket
s.close()


