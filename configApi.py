import os

os.system("apt-get install nginx")
os.system("apt-get install git")
os.system("wget -qO- https://deb.nodesource.com/setup_8.x | sudo -E bash -")
os.system("apt-get install -y nodejs")
os.system("apt-get install -y nodejs-legacy")
os.system("apt-get install npm")
os.system("npm install -g npm@latest")
os.system("npm install n")
os.system("n stable")
os.system("npm install -g pm2")
os.system("git clone https://github.com/guilhermecoelho/myacconts.git /var/www/myaccounts/code")
os.system("cd /var/www/myaccounts/code && pm2 start npm -n myaccount -- start")
