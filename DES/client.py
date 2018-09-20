import socket
import DES
 
def main():
        host = '127.0.0.1'
        port = 4500

        # start out with the key, CHANGE KEY HERE
        key10bit = '1010101010'
        k1, k2 = DES.generateKeys(key10bit)
        
        # bind the socket to host and port
        mySocket = socket.socket()
        # client does not need to bind, just connect!
        mySocket.connect((host,port)) 
        

        plain_text = input("Type a to start and q to quit:")
        # keep reading in data till user quits
        while plain_text != 'q': 
                mySocket.send(plain_text.encode())
                data = mySocket.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                plain_text = (input("Enter a 8 bit plain text => "))

                # unless they want to quit (which would bork up my function as of now), encrypt!
                if(plain_text.lower()=='q'):
                    continue

                # if it is not a 8bit, keep asking for somethin
                while(len(plain_text)!=8):
                    plain_text = (input("Must enter a 8 bit plain text => "))

                # encrypt and send!
                cipher_text = DES.encrypt(plain_text, k1, k2)
                print("Sending encrpted message to server:", cipher_text)
                plain_text = cipher_text
                 
        mySocket.close()
 
if __name__ == '__main__':
    main()
