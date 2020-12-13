

import socket



s = socket.socket()



PORT = 9898

print(" \n Server is listing on port :" , PORT, " \n")



s.bind(('', PORT))



s.listen(5)



file = open("received.txt", "wb") 

print(" \n Copied file name will be received.txt at server side\n ")

 

while True:

    conn, addr = s.accept()

    msg = "\n\n Hi Client **Welcome to Server**\n\n"

    conn.send(msg.encode())

    RecvData = conn.recv(1024)

    while RecvData:

        file.write(RecvData)

        RecvData = conn.recv(1024)

    file.close()

    print("\n File has been copied successfully \n")



    conn.close()

    print("\n Server closed the connection \n")





    break


