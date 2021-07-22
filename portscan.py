#!/usr/local/bin/python3

import socket
from termcolor import colored
from threading import *
import time

def portScan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    try:
        sock.connect((host,port))
        print(colored("[+] port %d open" %port,'green'))
    except:
        return
    finally:
        sock.close()

def main():
    
    host = input(colored("Enter target Host IP address: ", 'cyan'))
    for port in range(0, 65535):
        try:
            t = Thread(target=portScan, args = (host, port))
            while active_count()>100 :
                time.sleep(5)
            t.start()
            #portScan(host, port)
        except:
            print(colored("[!] Thread Error for port %d" % port, 'yellow'))



if __name__ == "__main__":
    main()
