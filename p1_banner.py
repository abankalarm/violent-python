#application banner grabbing

import optparse
import socket
import optparse
from socket import *

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('violentpython\r\n')
        results = connSkt.recv(100)
        print('[+]%d/tcp open'%tgtPort)
        print('[+]'+str(results))
        connSkt.close()
    except:
        print('[-] tcp closed'+str(tgtPort))

def portscan(tgtHost, tgtPort):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-]cannot resolve UNKNOWN HOST')
        return
    try:
        tgtName= gethostbyaddr(tgtIP)
        print('[+] scan results for' + tgtName[0])
    except:
        print('[+] scan results for'+ tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('scanning port'+ tgtPort)
        connScan(tgtHost,int(tgtPort))

def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', help= 'specify target host')
    parser.add_option('-p', dest='tgtPort', help= 'specify ports to scan')
    (options, args)= parser.parse_args()
    tgtHost = options.tgtHost
    global tgtPorts
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print parser.usage
        exit(0)
    portscan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()