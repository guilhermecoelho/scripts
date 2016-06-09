#!/bin/bash
#limpando tabelas
iptables -F &&
iptables -X &&
iptables -t nat -F &&
iptables -t nat -X &&

#Libera o loopback
iptables -A INPUT -i lo -j ACCEPT

#Libera SSh e  Web
iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp -m tcp --dport 3001 -j ACCEPT

iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

echo 1 > /proc/sys/net/ipv4/ip_forward &&
# Protecao contra port scanners ocultos
iptables -A INPUT -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit 1/s -j ACCEPT
# Bloqueando tracertroute
iptables -A INPUT -p udp -s 0/0 -i eth1 --dport 33435:33525 -j DROP
#Protecoes contra ataques
iptables -A INPUT -m state --state INVALID -j DROP

#habilita acesso aos containers
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to 10.0.3.93:3000
iptables -A FORWARD -p tcp -d 10.0.3.93 --dport 80 -j ACCEPT

#termina
echo "Iptables Pronto"
