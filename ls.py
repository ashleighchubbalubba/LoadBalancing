import time
import random
import socket

def ls(lsListenPort, ts1Hostname, ts1ListenPort): # ts2Hostname, ts2ListenPort)

    # create to client
    try:
        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    except socket.error as err: 
        exit()
    
    # connect to client
    server_binding = ('', lsListenPort)
    ls.bind(server_binding) 
    ls.listen(1) 
    csockid, addr = ls.accept()

    # create TS1 socket
    try:
        ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    except socket.error as err:
        exit()

    # connect to TS1 server
    ts1Addr = socket.gethostbyname(ts1Hostname)
    server_binding = (ts1Addr, ts1ListenPort)
    ts1.connect(server_binding)
    
    while(True):
        # Receive queried hostname from the client
        queriedHostname = csockid.recv(300).decode('utf-8').rstrip()
        
        # if client finished sending all hostnames, close socket
        if queriedHostname == "closeConnection":
            # send closing message to TS1 and TS2
            ts1.send("closeConnection".encode('utf-8'))
            # ts2.send("closeConnection".encode('utf-8'))
            break

        # send queriedHostname to TS1 and TS2
        ts1.send(queriedHostname.encode('utf-8'))

        receivedString = ts1.recv(300) # receive LS's answer
        receivedString = receivedString.decode('utf-8').rstrip() 

        # if we got a response from TS1 or TS2, send response to client
        
        # if we didn't get a response from TS1 or TS2, send error to client

        # send string to the client
        csockid.send(receivedString.encode('utf-8'))

    # close socket
    ls.close()
    ts1.close()
    # ts
    exit() 


if __name__ == "__main__":
    lsListenPort = 50007
    ts1Hostname = ""  # type in hostname of machine that TS1 runs on
    ts1ListenPort = 50008
    # ts2Hostname = ""  # type in hostname of machine that TS2 runs on
    # ts2ListenPort = 50009
    ls(lsListenPort, ts1Hostname, ts1ListenPort) #, ts2Hostname, ts2ListenPort)

    