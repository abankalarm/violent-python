import optparse
from p1_socket import *


def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket ( AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        print ('[+]%d/tcp open'%tgtPort)
        connSkt.close()

    except:
        print("[-]%d/tcp closed"% tgtPort)

def portScan(tgtHost,tgtPort):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-]cannot resolve '%s': UNKOWN HOST"%tgtHost)
        return
    try:
        tgtName = gethostbyaddress(tgtIP)
        print ('\n[+] scan results for:'+ tgtName[0])
    except:
        print ('[+ scan results for:' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print ('scanning port' + tgtPort)
        connScan(tgtHost, int(tgtPort))