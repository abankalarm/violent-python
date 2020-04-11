import optparse

parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
parser.add_option('-H', dest='tgtHost', help= 'specify target host')
parser.add_option('-p', dest='tgtPort', help= 'specify ports to scan')
(options, args)= parser.parse_args()
tgthost = options.tgtHost
tgtPort = options.tgtPort
if (tgtHost == None) | (tgtPort == None):
    print parser.usage
    exit(0)