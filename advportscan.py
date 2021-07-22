#!/usr/local/bin/python3

from termcolor import colored
from threading import *
import optparse
import sys
from socket import *


def connScan(tgtHost, port):
    setdefaulttimeout(2)
    sock = socket()
    try:
        sock.connect((str(tgtHost), port))
        print(colored("[+] %d/tcp is open" %port, 'green'))
    except:
        print(colored("[-] %d/tcp is closed" %port, 'red'))
    finally:
        sock.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIp= gethostbyname(tgtHost)
    except:
        print(colored("[-] Unknown Host %s" %tgtHost, 'red', attrs=['blink']))
    try:
        tgtname = gethostbyaddr(tgtIp)
        print(colored("[+] Scan result for %s @ %s " %(tgtname[0], tgtname[1]), 'cyan', attrs=['reverse']))
    except:
        print(colored("[+] scan result for %s" %tgtHost, 'cyan', attrs=['reverse']))
    
    for port in tgtPorts:
        try:
            t = Thread(target = connScan, args=(tgtHost, int(port)))
            t.start()
            #connScan(tgtHost, int(port))
        except:
            print(colored("[!] Unable to connect to port %d/tcp" %port, 'yellow', attrs=['blink']))


def main():
    parser = optparse.OptionParser(colored("[*] Usage of the Program: %s -H <Target Host> -P <target Ports list seperated by comma(,)" %(sys.argv[0]), 'magenta'))
    parser.add_option('-H', dest='tgtHost', type='string', help=colored("Specify target host", 'magenta'))
    parser.add_option('-P', dest='tgtPort', type='string', help=colored("Specify target ports seperated by comma(,)", 'magenta'))
    
    options,args = parser.parse_args()
    tgtHost = str(options.tgtHost)
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None)|(tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)
    

if __name__ == "__main__":
    main()
