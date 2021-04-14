import time
import random
import socket

def ts2(ts2ListenPort): 
    dnsTable = [] # list of arrays [ [hostname1, ip1, flag1], [hostname2, ip2, flag2],...]
    currInfo = [] # current line's info [hostname1,ip1,flag1]

    # populate the table while reading the file
    file = open('PROJ2-DNSTS2.txt', 'r')
    linesList = file.readlines()
    for line in linesList: 
        for word in line.split(): 
            currInfo.append(word) 
        dnsTable.append(currInfo)
        currInfo = []
    
    # connect to LS
    try:
        ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    except socket.error as err: 
        exit()
    
    # connect to LS server
    server_binding = ('', ts2ListenPort)
    ts2.bind(server_binding) 
    ts2.listen(1)  
    LSsockid, addr = ts2.accept()

    while True:
        # receive queried hostname from LS
        queriedHostname = LSsockid.recv(300).decode('utf-8').rstrip()

        # if LS finished sending all hostnames, close socket
        if queriedHostname == "closeConnection":
			break

        string = ""

        # search dnsTable for queried hostname 
        for info in dnsTable:
            replacement = info[0].lower()
            # check hostname of each list stored in DNSTable 
            if(replacement == queriedHostname):
                # there's a match! send "Hostname IPaddress A" to LS
                string = "" + info[0] + " " + info[1] + " " + info[2]
                LSsockid.send(string.encode('utf-8'))
                break        

    # Close the server socket
    ts2.close() 
    exit()   

if __name__ == "__main__":
    ts2ListenPort = 50009
    ts2(ts2ListenPort)