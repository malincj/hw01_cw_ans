#Task1

#Client Socket
import socket
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#Server access
cs.connect(("localhost",8181));
#receive data
receivedata = cs.recv(1024);
print('%s fromServer' % (receivedata.decode()))
