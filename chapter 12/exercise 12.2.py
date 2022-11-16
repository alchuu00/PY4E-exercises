import socket

try:
    inp = input("Enter webpage URL: ")
    host = inp.split("/")[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET ' + inp + 'HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    recieved = b""

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        recieved += data

    recieved = recieved.decode()
    print(recieved[:3000])
    print(len(recieved))

    mysock.close()
except:
    print("The URL you entered is not properly formatted or non-existent!")