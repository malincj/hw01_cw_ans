#Task2
import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#Listen port
socket.bind(("localhost",8181));
#Clients connect
socket.listen(2)
cnt = 1;
chk = '';

while cnt <= 2:
    (c, Addresses) = socket.accept();
    print("Connected %s:%s"%(Addresses[0], Addresses[1]));

    if cnt == 1:
        clientdata = c.recv(1024)
        tr = clientdata.decode();
        chk = int(tr);
        c.close();
    else :
        chk -= 1;
        c.send(str(chk).encode());
        c.close();
        break;

    cnt += 1
