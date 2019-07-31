#!/usr/bin/env python

import subprocess
import optparse
import re

def get_suid():
    print("[+] Searching for SUID files...")
    suid_found = subprocess.call(['find / -perm -u=s -type f 2>/dev/null'])
    
    if suid_found:
        print("[+] Found SUID files:\n " +
            suid_found)
    else:
        print("[-] Could not find SUID files.")

get_suid()
        
