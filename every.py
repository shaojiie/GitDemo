from telnet_test import TelnetClient


#command = 'cd sh /app1/yn5301/sj/main/every.sh'
command = 'cd /app1/yn5301/sj/main;sh every.sh'
print(command)
t =TelnetClient()
c_result = t.cmd_run(command)
print('============'+c_result)