
import os
import subprocess

print("Container name: ")
containerName = raw_input()

os.system("git clone  https://github.com/guilhermecoelho/scripts.git /tmp/script/")

os.system("apt-get install lxd")

os.system("lxc launch ubuntu:x "+containerName)

p = subprocess.Popen("lxc list "+containerName+" -c 4 | awk '!/IPV4/{ if ( $2 != \"\" ) print $2}'te", stdout=subprocess.PIPE, shell=True)
(ipContainer, err) = p.communicate()

os.system("iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to "+str(ipContainer)+":80")

os.system("lxc file push /tmp/script/configNginx.py  "+containerName+"/tmp/configNginx.py")

os.system("lxc exec "+containerName+" -- sudo apt-get install python")
print("lxc exec "+containerName+" -- sudo python /tmp/configNginx.py "+str(ipContainer))
os.system("lxc exec "+containerName+" -- sudo python /tmp/configNginx.py "+str(ipContainer))

os.system("rm -r /tmp/script/")
