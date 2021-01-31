#Task1
import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#Listen port
socket.bind(("localhost",8181));
#Clients connect
socket.listen(2)
cnt = 1;
chk = '';

while cnt <= 2:
    (c, Address) = socket.accept();
    print("Connected %s:%s"%(Address[0], Address[1]));

    if cnt == 1:
        clientdata = c.recv(1024)
        temp_str = clientdata.decode();
        chk = temp_str[0];
        c.close();
    else :
        chk = chr(ord(chk) - 1);
        c.send(chk.encode());
        c.close();
        break;
        sys(exit(0))

    cnt += 1
   
