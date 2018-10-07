
import os

print("Container name: ")
containerName = raw_input()

os.system("apt-get install lxc")
os.system("lxc-create -n "+containerName+" -t ubuntu")
os.system("lxc-start -n "+containerName+" -d")

ipContainer = os.system("lxc-info -n "+containerName+" -iH")
os.system("iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to "+str(ipContainer)+":80")





