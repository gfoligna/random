#!/usr/bin/env python

## Created by Gonzalo Foligna (gfoligna@gmail.com) ##
## Created because I needed something to alert if my external IP changes ##
## It uses 'notify-send' as the notifier ##

import requests
import os

def current_ip_empty():
    f = open('/tmp/ip', 'rt')
    f.read
    f.close
    if len(f) == 0:
        r = requests.get('http://ifconfig.co/ip')
        output = (r.text).replace('\n', '')
        #print output
        f = open('/tmp/ip')
        f.write(output)
        f.close

def compare_ips():
    current_ip_empty
    if os.path.isfile('/tmp/ip') == False:
        os.mknod('/tmp/ip')
    f = open('/tmp/ip')
    old_ip = f.read()
    f.close
    r = requests.get('http://ifconfig.co/ip')
    new_ip = (r.text).replace('\n', '')
    print 'Current IP: '+new_ip
    print 'Old IP: '+str(old_ip)
    if str(new_ip) != str(old_ip):
        f = open('/tmp/ip', 'wt')
        f.write(new_ip)
        f.close
        cmd = "/usr/bin/notify-send External-IP-Changed "+new_ip
        os.system(cmd)

compare_ips()
