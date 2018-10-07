import sys
import os

def confNginx(ip):
    strConfig = str("server { \n" 
    "  listen 80;\n"
    "  server_name tddnode.com;\n"
    "  location / {\n"
    "    proxy_pass       http://"+ip+";\n"
    "    proxy_set_header Host              $host;\n"
    "    proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;\n"
    "    proxy_set_header X-Forwarded-Proto $scheme;\n"
    "    proxy_set_header Accept-Encoding   '';\n"
    "  }\n"
    "}\n")

    file = open("/etc/nginx/sites-available/default", "w")
    file.truncate(0)
    file.write(strConfig)
    file.close()

os.system("apt-get install nginx")
confNginx(sys.argv[1])
