
import os

print("Container name: ")
containerName = raw_input()

os.system("apt-get install lxd")

os.system("lxc launch ubuntu "+containerName+")
os.system("lxc-start -n "+containerName+" -d")

ipContainer = str(os.system("lxc list "+containerName+" -c 4 | awk '!/IPV4/{ if ( $2 != "" ) print $2}'"))
          
os.system("iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to "+ipContainer+":80")





