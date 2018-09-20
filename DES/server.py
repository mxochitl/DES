import socket
import DES
 
def Main():
    host = "127.0.0.1"
    port = 4500

    # start out with the key, CHANGE KEY HERE
    key10bit = '1010101010'
    k1, k2 = DES.generateKeys(key10bit)
    
    # bind the socket to host and port
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    # pass 1 to the listen socket so it listens forever
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))

    # run untill connection is closed
    while True:
            # must decode connection bc normal string won’t pass through socket 
            # str does not implement buffer interface 
            data = conn.recv(1024).decode()
            if not data:
                    break
            # if this is the first time, don't call any decodeing/ encrypting functions
            if data.lower() == 'a':
                conn.send(data.encode())
                continue

            print ("from connected  user: " + str(data))
            data = str(data)
            print ("sending: " + str(data))
            # calls decrypt function on recieved encrypted message
            plain_txt = DES.decrypt(data, k1, k2)
            # send back decrypted message (plain text)
            conn.send(plain_txt.encode())
    # close the connection
    conn.close()
     
if __name__ == '__main__':
    Main()