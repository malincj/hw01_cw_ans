#Task 1

#Client Socket
import socket
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#Server access
cs.connect(("localhost",8181));
#Send to server
data = "B";
cs.send(data.encode());
print('%s ToServer' % (data))
