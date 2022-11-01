import port_scanning, dnsLookup, network, websockets
# Log all of this data
import json
import logging

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
    logging.debug(f'Your Public IP is: {network.check_public_ip()}')
else:
    print("Not connected to the internet.")
    logging.error("Not connected to the internet.")
    exit()
print("\n")

logging.info("Nameservers and IP Address:")
print("Basic connectivity 2: Nameservers and IP Addresses")
print("\n")
if (dnsLookup.get_nameservers(DOMAIN) != False):
    for val in dnsLookup.get_nameservers(DOMAIN):
        print(f"{val[0]} | {val[1]}")
        logging.debug(f"{val[0]} | {val[1]}")
    print("\n")

    if (dnsLookup.get_ip_address(DOMAIN) != False):
        print(f"{val[0]} | {val[1]}")
        logging.debug(f"{val[0]} | {val[1]}")
    else:
        print("Domain doesn't exist.")
        logging.error("Domain doesn't exist.")
else:
    print("Nameservers don't exist.")
    logging.error("Nameservers don't exist.")

print("\n")

logging.info("Websocket connectivity tests:")
print("Basic connectivity 3: Websocket connectivity test\n")
if (websockets.websocket_test_connection()[0] == True):
    print("Connection Established.")
    logging.debug("Connection established.")
else:
    print("Connection Failed.")
    logging.error("Connection failed.")

if (websockets.websocket_test_connection()[1] == True):
    print("Message sent.")
    logging.debug("Message sent.")
else:
    print("Message not sent.")
    logging.error("Message not sent.")

if (websockets.websocket_test_connection()[2] == True):
    print("Message received.")
    logging.debug("Message received.")
else:
    print("Message not received.")
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
            print(f"{port[0]}:{port[1]} - Listening to TCP Signals")
            logging.debug(f"{port[0]}:{port[1]} - Listening to TCP Signals")
        else:
            print(f"{port[0]}:{port[1]} - Not listening to TCP Signals")
            logging.error(f"{port[0]}:{port[1]} - Not listening to TCP Signals")

        if (port_scanning.check_for_udp(port[0], port[1])):
            print(f"{port[0]}:{port[1]} - Listening to UDP Signals")
            logging.debug(f"{port[0]}:{port[1]} - Listening to UDP Signals")
        else:
            print(f"{port[0]}:{port[1]} - Not listening to UDP Signals")
            logging.error(f"{port[0]}:{port[1]} - Not listening to UDP Signals")
        
    print("\n")

    for url in lte['urls']:
        #print(check_wget(url))
        if (port_scanning.check_wget(url)):
            print(f"{url} - Accessible.")
            logging.debug(f"{url} - Accessible.")
        else:
            print(f"{url} - Not accessible.")
            logging.error(f"{url} - Not accessible.")

    print("\n")

    print("WIFI:")
    for port in wifi['ports']:
        if (port_scanning.check_for_tcp(port[0], port[1])):
            print(f"{port[0]}:{port[1]} - Listening to TCP Signals")
            logging.debug(f"{port[0]}:{port[1]} - Listening to TCP Signals")
        else:
            print(f"{port[0]}:{port[1]} - Not listening to TCP Signals")
            logging.error(f"{port[0]}:{port[1]} - Not listening to TCP Signals")

        if (port_scanning.check_for_udp(port[0], port[1])):
            print(f"{port[0]}:{port[1]} - Listening to UDP Signals")
            logging.debug(f"{port[0]}:{port[1]} - Listening to UDP Signals")
        else:
            print(f"{port[0]}:{port[1]} - Not listening to UDP Signals")
            logging.error(f"{port[0]}:{port[1]} - Not listening to UDP Signals")

        
    print("\n")
    for url in wifi['urls']:
        if (port_scanning.check_wget(url)):
            print(f"{url} - Accessible.")
            logging.debug(f"{url} - Accessible.")
        else:
            print(f"{url} - Not accessible.")
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