import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 8080
s.bind(('',port))
s.listen(1)
print("waiting for incomming connections.....")

conn, addr = s.accept()
print(addr, "has connected to the server")

 
conn.send(b'welcome to online TCP Arithmatic calculator')
a1 = conn.recv(1024)
a2 = str(a1, 'utf8')
num1 = int(a2)
print('your 1st no. is = ')
print(num1)
b1 = conn.recv(1024)
b2 = str(b1, 'utf8')
num2 = int(b2)
print('your 2nd no. is = ')
print(num2)
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
print("sending addition.....")
timer = int(5)
while (timer != 0 ):
        timer = timer-1
        time.sleep(1)
        print(timer)
conn.send(bytes(str(addition),  'utf8'))
print("sending subtraction.....")
timer = int(5)
while (timer != 0 ):
        timer = timer-1
        time.sleep(1)
        print(timer)
conn.send(bytes(str(subtraction), 'utf8'))
print("sending multiplication.....")
timer = int(5)
while (timer != 0 ):
        timer = timer-1
        time.sleep(1)
        print(timer)
conn.send(bytes(str(multiplication), 'utf8'))
print("sending division.....")
timer = int(5)
while (timer != 0 ):
        timer = timer-1
        time.sleep(1)
        print(timer)
conn.send(bytes(str(division), 'utf8'))

print('all operations are done :)')
conn.close()
