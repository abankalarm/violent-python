import optparse
from p1_socket import *


def connScan(tgthost,tgtport):
    try:
        connSkt = socket ( AF_INET, SOCK_STREAM)
        connSkt.connect((tgthost,tgtport))
        print ('[+]%d/tcp open'%tgtport)
        connSkt.close()

    except:
        print("[-]%d/tcp closed"% tgtport)

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