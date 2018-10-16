
import os
import subprocess
import time

global containerName
global ipContainer


def createContainer():
    global containerName
    global ipContainer

    print("Container name: ")
    containerName = raw_input()

    os.system("git clone  https://github.com/guilhermecoelho/scripts.git /tmp/script/")

    os.system("apt-get install lxd")

    os.system("lxc launch ubuntu:x "+containerName)
 
    #need wait a time to mapping container IP
    os.system("lxc list")
    time.sleep(10)
    os.system("lxc list")

    p = subprocess.Popen("lxc list "+containerName+" -c 4 | awk '!/IPV4/{ if ( $2 != \"\" ) print $2}'te", stdout=subprocess.PIPE, shell=True)
    (ipContainer, err) = p.communicate()

    print "lxc exec "+containerName+" -- sudo apt-get update"
    os.system("lxc exec "+containerName+" -- sudo apt-get update")

    print "lxc exec "+containerName+" -- sudo apt-get install python"
    os.system("lxc exec "+containerName+" -- sudo apt-get install python")

    os.system("iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to "+str(ipContainer)+":80")

def configNginx():
    global containerName
    global ipContainer

    print "lxc file push /tmp/script/configNginx.py  "+containerName+"/tmp/configNginx.py"
    os.system("lxc file push /tmp/script/configNginx.py  "+containerName+"/tmp/configNginx.py")

    print "lxc exec "+containerName+" -- sudo python /tmp/configNginx.py "+str(ipContainer)
    os.system("lxc exec "+containerName+" -- sudo python /tmp/configNginx.py "+str(ipContainer))

def configMongo():
    global containerName
    global ipContainer

    os.system("lxc file push /tmp/script/configMongo.py  "+containerName+"/tmp/configMongo.py")
    os.system("lxc exec "+containerName+" -- sudo python /tmp/configMongo.py "+str(ipContainer))

def start():
    print("Select Option: \n 1 - nginx\n 2 - mongodb\n 3 - all")
    option = raw_input()

    if option == "1":
        createContainer()
        configNginx()
    if option == "2":
        createContainer()
        configMongo()
    if option == "3":
        createContainer()
        configNginx()
        createContainer()
        configMongo()


start()

os.system("rm -r /tmp/script/")
