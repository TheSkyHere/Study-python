#!/usr/bin/python3
import os,sys
bmc_hostname = "10.204.30.185"

os.system("ssh-keygen -f ~/.ssh/known_hosts -R {}".format(bmc_hostname))