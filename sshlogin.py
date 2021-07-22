#!/usr/local/bin/python3

import pexpect

prompt = ["# ", ">>> ", "> ", "\$ ", "~$ ", "\% "]


def connect(user, host, password):
    ssh_newkey = "Are you sure you want to continue connecting"
    
    conn_str = "ssh "+user+"@"+host
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    
    if ret == 0:
        print("[-] Error in connection")
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print("[-] Error in connection")
            return
    child.sendline(password)
    child.expect(prompt)
    return child
    
    
def send_cmd(child, cmd):
    child.sendline(cmd)
    child.expect(prompt)
    print(child.before)
    """result = str(child.before).split("\n")
    for line in result:
        print(line)"""
    

def main():
    host = "172.20.10.6"
    user = "msfadmin"
    password = 'msfadmin'
    
    child = connect(user, host, password)
    #send_cmd(child, 'cat /etc/shadow | grep root; ps')
    send_cmd(child, "nmap 172.20.10.6; ps")


if __name__ == "__main__":
    main()
