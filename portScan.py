import optparse
import socket
from socket import *

# Testing connection to ports
def connScan(tgtHost, tgtPort):
    try:
        connSocket=socket(AF_INET, SOCK_STREAM)
        connSocket.connect((tgtHost,tgtPort))
        connSocket.send('Excelsior\r\n')
        results=connSocket.recv(100)
        print(f'[+] {tgtPort}/tcp Open')
        print(f'[+] {str(results)}')
        connSocket.close()
    except:
        print(f'[-] {tgtPort}/tcp Closed')
    

       
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)    # Will attempt to resolve host to IPv4
        print(tgtIP)
    except:
        print(f'[-] Cannot resolve {tgtHost}: Unknown Host.')
        return
    
    try:
        tgtName=gethostbyaddr(tgtIP)
        print(f'\n[+] Scan Results for: {tgtName[0]}')
    except:
        print(f'[+] Scan Results for: {tgtIP}')
    setdefaulttimeout(1)
    
    for tgtPort in tgtPorts:
        print(f'Scanning port {tgtPort}')
        connScan(tgtHost, int(tgtPort))
        
                

# Uses optParse to instruct on script usage
def main():
    parser = optparse.OptionParser('usage %prog -H ' + '<target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='int', help='specify target port')

    (options, args) = parser.parse_args()

    tgtHost=options.tgtHost
    tgtPorts=str(options.tgtPort).split(', ')

    if (tgtHost == None) | (tgtPorts == None):
        print('[-] You must specify a target host name and port[s].')
        print(parser.usage)
        exit(0)
        
    portScan(tgtHost, tgtPorts)

#print(parser.usage)

if __name__ == '__main__':
    main()