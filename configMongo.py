import sys
import os

def confMongo(ip):
    strConfig = str("# mongodb.conf\n"
        "# Where to store the data.\n"
        "dbpath=/var/lib/mongodb\n"
        "#where to log\n"
        "logpath=/var/log/mongodb/mongodb.log\n"
        "logappend=true\n"
        "bind_ip = "+ip+"\n"
        "port = 27017\n"
        "# Enable journaling, http://www.mongodb.org/display/DOCS/Journaling\n"
        "journal=true")

    file = open("/etc/mongodb.conf", "w")
    file.truncate(0)
    file.write(strConfig)
    file.close()


os.system("apt-get install -y mongodb")
confMongo(sys.argv[1])
os.system("service mongodb restart")
