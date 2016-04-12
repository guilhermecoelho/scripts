#!/bin/bash
iptables -t nat -A PREROUTING -i eth0 -j DNAT --to 10.0.3.154
