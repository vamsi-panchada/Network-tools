#!/usr/local/bin/python3
import socket
from threading import *
import time
from termcolor import colored


def retBanner(ip, port):
    socket.setdefaulttimeout(2)
    s = socket.socket()
    try:
        s.connect((ip, port))
        banner = s.recv(1024)
        if banner:
            print("port %d: %s"%(port,banner))
    except:
        return
    finally:
        s.close()


def main():
    ip = input("Enter target host IP: ")
    for port in range(1,65535):
        banner = retBanner(ip, port)
        try:
            t = Thread(target=retBanner, args = (ip,port))
            while active_count() > 100 :
                time.sleep(5)
            t.start()
        except:
            print(colored('Thread error','red'))

if __name__=="__main__":
    main()
