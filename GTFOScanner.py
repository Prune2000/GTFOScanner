#!/usr/bin/env python

import os
import optparse
import re

def get_suid():
    print("[+] Searching for SUID files...")
    suid_found = os.system('find / -perm -u=s -type f 2>/dev/null')

    if suid_found:
        print("[+] Comparing SUID files found to the GTFO list...")

    else:
        print("[-] Could not find SUID files.")

get_suid()
