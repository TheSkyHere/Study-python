#!/usr/bin/python3
import os
import time
import pexpect
import logging

log = logging.getLogger(__name__)


def test_nic():
    out=pexpect.spawn('/home/admin/bf-sde-9.3.1-1.01.00/install/bin/bfshell')
    time.sleep(1)
    out.sendline("ucli \n")
    time.sleep(1)
    out.sendline("pm \n")
    time.sleep(1)
    out.sendline("show \n")
    out.expect("bf-sde", timeout=10)
    log.info("test")
    log.info("test" + str(out.before))
    time.sleep(1)
    return True


test_nic()