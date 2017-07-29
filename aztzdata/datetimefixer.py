#!/usr/local/bin/python3.4

import paramiko
from scp import SCPClient
import os
import time

ippass = (os.getcwd()+'/ippass')

with open(ippass) as ippassfile:
    siyahi = ippassfile.readlines() 
    for line in siyahi:
        ipad = line.split()[0]
        passw = line.split()[1]

        buff = ''
        resp = ''

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ipad, username='root', password=passw, look_for_keys=False, allow_agent=False)
        
        scp = SCPClient(ssh.get_transport())
        scp.put(os.getcwd()+'/asia', '/root/asia')
        scp.close()

        chan = ssh.invoke_shell()
        chan.send('zic /root/asia\n')
        time.sleep(1)

        chan.send('tzdata-update\n')
        time.sleep(1)
        ssh.close()
