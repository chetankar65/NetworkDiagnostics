import os
import scapy.all as scapy
from scapy.config import conf
# getting public IP address
def check_public_ip():
    externalIP  = os.popen('curl -s ifconfig.me').readline()
    if (len(externalIP) == 0):
        return 0
    else:
        return externalIP

# get network details 
def network_details():
    s = list() 
    for line in scapy.read_routes():
        if (line[2] != "0.0.0.0"):
            data_dict = {'Interface' : line[3], 'Gateway' : line[2], 'output_ip' : line[4]}
            s.append(data_dict)

    return (s)
