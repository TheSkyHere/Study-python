#!/usr/bin/python3
import syslog,sys,os
import fcntl

#log path：/var/log/syslog 和 /var/log/messages
#？？？log中没有看到priority信息

syslog.syslog(syslog.LOG_ERR,'1: set_host_cpu_power failed')
syslog.syslog(syslog.LOG_EMERG,'2: set_host_cpu_power failed')
syslog.syslog(syslog.LOG_ALERT,'3: set_host_cpu_power failed')
syslog.syslog(syslog.LOG_WARNING,'4: set_host_cpu_power failed')
syslog.syslog(syslog.LOG_NOTICE,'5: set_host_cpu_power failed')
syslog.syslog(syslog.LOG_INFO,'6: set_host_cpu_power failed')
syslog.syslog(syslog.LOG_DEBUG,'7: set_host_cpu_power failed')

