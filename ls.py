import time
import random
import socket

def ls(lsListenPort, ts1Hostname, ts1ListenPort, ts2Hostname, ts2ListenPort):

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
    ts1.settimeout(5)

    # create TS2 socket
    try:
        ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    except socket.error as err:
        exit()

    # connect to TS2 server
    ts2Addr = socket.gethostbyname(ts2Hostname)
    server_binding = (ts2Addr, ts2ListenPort)
    ts2.connect(server_binding)
    ts2.settimeout(5)
    
    while(True):
        # Receive queried hostname from the client
        queriedHostname = csockid.recv(300).decode('utf-8').rstrip()
        
        # if client finished sending all hostnames, close socket
        if queriedHostname == "closeConnection":
            # send closing message to TS1 and TS2
            ts1.send("closeConnection".encode('utf-8'))
            ts2.send("closeConnection".encode('utf-8'))
            break

        # send queriedHostname to TS1
        ts1.send(queriedHostname.encode('utf-8'))
        ts2.send(queriedHostname.encode('utf-8'))

        # if we got a response from TS1, send response to client
        try:
            receivedString = ts1.recv(300).decode('utf-8').rstrip() # receive TS1's answer
            csockid.send(receivedString.encode('utf-8')) # send string to the client
        # if we didn't get a response from TS1, send error to client
        except socket.timeout:
            try:
                receivedString = ts2.recv(300).decode("utf-8").rstrip()
                csockid.send(receivedString.encode("utf-8"))
            except socket.timeout:
                errorMessage = "" + queriedHostname + " - Error:HOST NOT FOUND"
                csockid.send(errorMessage.encode('utf-8')) # send string to the client

    # close socket
    ls.close()
    ts1.close()
    ts2.close()
    exit() 


if __name__ == "__main__":
    lsListenPort = 50007
    ts1Hostname = ""  # type in hostname of machine that TS1 runs on
    ts1ListenPort = 50008
    ts2Hostname = ""  # type in hostname of machine that TS2 runs on
    ts2ListenPort = 50009
    ls(lsListenPort, ts1Hostname, ts1ListenPort, ts2Hostname, ts2ListenPort)

    