
import time
import os
from datetime import datetime as dt

host_temp = "hosts"
host_file = "/etc/hosts"
LOCALHOST = "127.0.0.1"
websites_list = ["www.facebook.com", "facebook.com"]

while True:
    print("running")
    if dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 3):
        with open(host_file, 'r+') as hostfile:
            content = hostfile.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    hostfile.write(LOCALHOST+" "+website+"\n")
    else:
        with open(host_file, 'r+') as hostfile:
            content = hostfile.readlines()
            hostfile.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    hostfile.write(line)
                hostfile.truncate()

    time.sleep(5)
