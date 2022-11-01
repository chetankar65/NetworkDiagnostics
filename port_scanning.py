import socket
import urllib.request as request
import json

timeout = 1.5
# checking if the port and domain is listening for TCP signals
def check_for_tcp(domain, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((domain, int(port)))
        sock.shutdown(socket.SHUT_RDWR)
        return True
    except Exception as err:
        return False
    finally:
        sock.close()

# checking if the port and domain is listening for UDP signals
def check_for_udp(domain, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    try:
        sock.connect((domain, int(port)))
        sock.shutdown(socket.SHUT_RDWR)
        return True
    except Exception as err:
        return False
    finally:
        sock.close()

# check if a url/ website is available and accessible
def check_wget(url):
    try:
        request.urlopen(url)
        # print(result.read())
        return True
    except Exception as err:
        # print(str(err))
        return False
        
# get data from a config.json
def read_config_file(file):
    # Validating a config json file
    try:
        f = open(file)
        data = json.load(f)
        lte = data["LTE"]
        wifi = data["WiFi"]
        print('LTE:\n')
        for port in lte['ports']:
            # print(check_for_tcp(port[0], port[1]))
            # print(check_for_udp(port[0], port[1]))

            if (check_for_tcp(port[0], port[1])):
                print(f"{port[0]}:{port[1]} - Listening to TCP Signals")
            else:
                print(f"{port[0]}:{port[1]} - Not listening to TCP Signals")

            if (check_for_udp(port[0], port[1])):
                print(f"{port[0]}:{port[1]} - Listening to UDP Signals")
            else:
                print(f"{port[0]}:{port[1]} - Not listening to UDP Signals")
        
        print("\n")

        for url in lte['urls']:
            #print(check_wget(url))
            if (check_wget(url)):
                print(f"{url} - Accessible.")
            else:
                print(f"{url} - Not accessible.")

        print("\n")
        print("WIFI:")
        for port in wifi['ports']:
            if (check_for_tcp(port[0], port[1])):
                print(f"{port[0]}:{port[1]} - Listening to TCP Signals")
            else:
                print(f"{port[0]}:{port[1]} - Not listening to TCP Signals")

            if (check_for_udp(port[0], port[1])):
                print(f"{port[0]}:{port[1]} - Listening to UDP Signals")
            else:
                print(f"{port[0]}:{port[1]} - Not listening to UDP Signals")
        
        print("\n")

        for url in wifi['urls']:
            if (check_wget(url)):
                print(f"{url} - Accessible.")
            else:
                print(f"{url} - Not accessible.")
        # iterating through ports and urls and running tests
    except ValueError:
        print("JSON Config format not correct")
    except FileNotFoundError:
        print("File not found")
    except KeyError:
        print("Key is not present")
    finally:
        f.close()

