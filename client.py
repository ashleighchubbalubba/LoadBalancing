import time
import random
import socket

def client(lsHostname, lsListenPort):
    # list that contains all queried hostnames
    hostnameList = []

    # populate hostNameList with hostnames from 'PROJ2-HNS.txt'(one line of the file = one element of hostnameList) 
    file = open('PROJ2-HNS.txt', 'r')
    linesList = file.readlines()
    for line in linesList: 
        hostnameList.append(line.lower())

    # create LS socket 
    try:
        csLS = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    except socket.error as err:
        exit()

    # connect to LS server
    lsAddr = socket.gethostbyname(lsHostname)
    server_binding = (lsAddr, lsListenPort)
    csLS.connect(server_binding)

    # iterate through each hostName to talk to servers
    for hostname in hostnameList: 
        csLS.send(hostname.encode('utf-8'))  # send queried hostname to LS

        receivedString = csLS.recv(300) # receive LS's answer
        receivedString = receivedString.decode('utf-8').rstrip() 

        # write to RESOLVED.txt file
        with open('RESOLVED.txt', 'a') as the_file:
            the_file.write(receivedString)
            the_file.write("\n")

    # if done going going through hostnames, tell LS to close connection
    csLS.send("closeConnection".encode('utf-8'))

    # close both sockets
    csLS.close()
    exit()

if __name__ == "__main__":
    lsHostname = ""      # type in hostname of machine that LS runs on
    lsListenPort = 50007
    
    client(lsHostname, lsListenPort)