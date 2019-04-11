import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 8080
s.connect(('127.0.0.1',port))
print("connected........")




print(s.recv(1024))

a = int(input('enter first no = '))
s.send(bytes(str(a), 'utf8'))
b = int(input('enter second no = '))
s.send(bytes(str(b), 'utf8'))
print('addition of numbers is: ')
s1= s.recv(1024)
s2= str(s1, 'utf8')
s3= int(s2)
print(s3)
print('subtration of numbers is: ')
d1= s.recv(1024)
d2= str(d1, 'utf8')
d3= int(d2)
print(d3)
print('multiplication of numbers is: ')
m1= s.recv(1024)
m2= str(m1, 'utf8')
m3= int(m2)
print(m3)
print('division of numbers is: ')
c1= s.recv(1024)
c2= str(c1, 'utf8')
print(c2)
s.close()


