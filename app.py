import port_scanning, dnsLookup, network, websockets
# Log all of this data
import json
import logging

#### adding color to python text
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
##############

logging.basicConfig(filename = 'log.log', level = logging.DEBUG)
DOMAIN = "google.com"
### IP, Gateway check
logging.info("Basic connectivity:")
logging.info("Local IP | Gateway")
print("Local IP | Gateway")
for x in network.network_details():
    print(f"{x['output_ip']} | {x['Gateway']}")
    logging.debug(f"{x['output_ip']} | {x['Gateway']}")

### checking internet connectivity
print("\n")
print("Basic connectivity 1: Internet connectivity")
print("\n")

logging.info("Public IP:")
if (network.check_public_ip() != 0):
    print('Your Public IP is: ', network.check_public_ip())
    logging.debug(f'Your Public IP is: {bcolors.OKGREEN} {network.check_public_ip()} {bcolors.ENDC}')
else:
    print(f"{bcolors.FAIL}Not connected to the internet.{bcolors.ENDC}")
    logging.error("Not connected to the internet.")
    exit()
print("\n")

logging.info("Nameservers and IP Address:")
print("Basic connectivity 2: Nameservers and IP Addresses")
print("\n")
if (dnsLookup.get_nameservers(DOMAIN) != False):
    for val in dnsLookup.get_nameservers(DOMAIN):
        print(f"{bcolors.OKCYAN} {val[0]} | {val[1]} {bcolors.ENDC}")
        logging.debug(f"{val[0]} | {val[1]}")
    print("\n")

    if (dnsLookup.get_ip_address(DOMAIN) != False):
        print(f"{bcolors.OKCYAN} {val[0]} | {val[1]} {bcolors.ENDC} ")
        logging.debug(f"{val[0]} | {val[1]}")
    else:
        print(f"{bcolors.FAIL}Domain doesn't exist.{bcolors.ENDC}")
        logging.error("Domain doesn't exist.")
else:
    print(f"{bcolors.FAIL}Nameservers don't exist. {bcolors.ENDC}")
    logging.error("Nameservers don't exist.")

print("\n")

logging.info("Websocket connectivity tests:")
print("Basic connectivity 3: Websocket connectivity test\n")
if (websockets.websocket_test_connection()[0] == True):
    print(f"{bcolors.OKGREEN}Connection Established.{bcolors.ENDC}")
    logging.debug("Connection established.")
else:
    print(f"{bcolors.FAIL}Connection Failed.{bcolors.ENDC}")
    logging.error("Connection failed.")

if (websockets.websocket_test_connection()[1] == True):
    print(f"{bcolors.OKGREEN}Message sent.{bcolors.ENDC}")
    logging.debug("Message sent.")
else:
    print(f"{bcolors.FAIL}Message not sent.{bcolors.ENDC}")
    logging.error("Message not sent.")

if (websockets.websocket_test_connection()[2] == True):
    print(f"{bcolors.OKGREEN}Message received.{bcolors.ENDC}")
    logging.debug("Message received.")
else:
    print(f"{bcolors.FAIL}Message not received.{bcolors.ENDC}")
    logging.error("Message not received.")

print("\n")

logging.info("WiFi/LTE Tests:")
print("WiFi/LTE:")
print("\n")

file = "config.json"
# Validating a config json file
try:
    f = open(file)
    data = json.load(f)
    lte = data["LTE"]
    wifi = data["WiFi"]
    print('LTE:')
    for port in lte['ports']:
        if (port_scanning.check_for_tcp(port[0], port[1])):
            print(f"{bcolors.OKGREEN}{port[0]}:{port[1]} - Listening to TCP Signals{bcolors.ENDC}")
            logging.debug(f"{port[0]}:{port[1]} - Listening to TCP Signals")
        else:
            print(f"{bcolors.FAIL}{port[0]}:{port[1]} - Not listening to TCP Signals {bcolors.ENDC}")
            logging.error(f"{port[0]}:{port[1]} - Not listening to TCP Signals")

        if (port_scanning.check_for_udp(port[0], port[1])):
            print(f"{bcolors.OKGREEN}{port[0]}:{port[1]} - Listening to UDP Signals{bcolors.ENDC}")
            logging.debug(f"{port[0]}:{port[1]} - Listening to UDP Signals")
        else:
            print(f"{bcolors.FAIL}{port[0]}:{port[1]} - Not listening to UDP Signals{bcolors.ENDC}")
            logging.error(f"{port[0]}:{port[1]} - Not listening to UDP Signals")
        
    print("\n")

    for url in lte['urls']:
        #print(check_wget(url))
        if (port_scanning.check_wget(url)):
            print(f"{bcolors.OKGREEN}{url} - Accessible.{bcolors.ENDC}")
            logging.debug(f"{url} - Accessible.")
        else:
            print(f"{bcolors.FAIL}{url} - Not accessible.{bcolors.ENDC}")
            logging.error(f"{url} - Not accessible.")

    print("\n")

    print("WIFI:")
    for port in wifi['ports']:
        if (port_scanning.check_for_tcp(port[0], port[1])):
            print(f"{bcolors.OKGREEN}{port[0]}:{port[1]} - Listening to TCP Signals {bcolors.ENDC}")
            logging.debug(f"{port[0]}:{port[1]} - Listening to TCP Signals")
        else:
            print(f"{bcolors.FAIL} {port[0]}:{port[1]} - Not listening to TCP Signals {bcolors.ENDC}")
            logging.error(f"{port[0]}:{port[1]} - Not listening to TCP Signals")

        if (port_scanning.check_for_udp(port[0], port[1])):
            print(f"{bcolors.OKGREEN} {port[0]}:{port[1]} - Listening to UDP Signals {bcolors.ENDC}")
            logging.debug(f"{port[0]}:{port[1]} - Listening to UDP Signals")
        else:
            print(f"{bcolors.FAIL} {port[0]}:{port[1]} - Not listening to UDP Signals {bcolors.ENDC}")
            logging.error(f"{port[0]}:{port[1]} - Not listening to UDP Signals")

        
    print("\n")
    for url in wifi['urls']:
        if (port_scanning.check_wget(url)):
            print(f"{bcolors.OKGREEN}{url} - Accessible.{bcolors.ENDC}")
            logging.debug(f"{url} - Accessible.")
        else:
            print(f"{bcolors.FAIL} {url} - Not accessible. {bcolors.ENDC}")
            logging.error(f"{url} - Not accessible.")
        # iterating through ports and urls and running tests
except ValueError:
    print("JSON Config format not correct")
    logging.error("JSON Config format not correct.")
except FileNotFoundError:
    print("File not found")
    logging.error("File not found.")
except KeyError as err:
    print("Key is not present")
    logging.error(str(err))
finally:
    f.close()