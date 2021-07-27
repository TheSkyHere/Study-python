import logging
import telnetlib
import time
import paramiko
import subprocess

class TelnetClient():
    def __init__(self):
        self.tn = telnetlib.Telnet()
        # logging.basicConfig(filename="log.log", level=logging.INFO)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def login_host(self, host_ip, username, password):
        try:
            self.tn = telnetlib.Telnet(host_ip, port=23)
        except:
            return False
        time.sleep(1)
        self.tn.read_until(b'User Name', timeout=5)
        self.tn.write(username.encode('ascii') + b'\r\n')
        time.sleep(1)
        self.tn.read_until(b'Password', timeout=5)
        self.tn.write(password.encode('ascii') + b'\r\n')
        time.sleep(2)
        command_result = self.tn.read_very_eager().decode('ascii')
        show_split = command_result.split('\r\n')
        if 'apc>' in show_split:
            self.logger.info("%s telnet login successfully.." % host_ip)
            return True
        else:
            self.logger.error("%s telnet login fail..." % host_ip)
            return False

    def execute_some_command(self, command):
        self.tn.write(command.encode('ascii') + b'\n')
        time.sleep(2)
        command_result = self.tn.read_very_eager().decode('ascii')
        show_split = command_result.split("\r\n")
        if "E000: Success" in show_split:
            self.logger.info("command executed successfully %s" % command)
            return True
        else:
            self.logger.info("command executed fail %s" % command)
            return False

    def logout_host(self):
        self.tn.write(b"exit\n")

def getsensors(ip):
    ssh = paramiko.SSHClient()
    know_host = paramiko.AutoAddPolicy()
    ssh.set_missing_host_key_policy(know_host)
    ssh.connect(ip,22,"sysadmin","superuser")
    #stdin, stdout, stderr = self.ssh.exec_command("cd /var/log/fw/")
    stdin, stdout, stderr = ssh.exec_command("ipmitest sensor list")
    #self.logger.info(stdout.read().decode())
    print(stdout.read().decode())
    ssh.close()

def runcommand(cmd):
    output = subprocess.getoutput(cmd)
    print(output)
    
def acpdu(command):
    client = TelnetClient()
    client.login_host("10.204.112.59","morton","morton2021")
    client.execute_some_command(command)
    time.sleep(2)
    client.logout_host()
    time.sleep(2)

for i in range(1,21,1):
    print("======================%d======================" % i)
    acpdu("olOff 12")
   # acpdu("olOff 16")
    time.sleep(3)
    acpdu("olOn 12")
   # acpdu("olOn 16")
    time.sleep(7200)    
    #print("----------wait for 2hours for next loop------------")

