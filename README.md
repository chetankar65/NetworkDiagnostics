# NetworkDiagnostics

Run using  - python3 app.py

Requirements (python modules):
- JSON
- logging

- Python dns module
- Scapy
- Socket/ urllib
- websocket

Simple network diagnostics tool written in Python with the help of scapy module. Can be used for setting up WiFi Routers/ access points etc.

Performs the following tests -

1. Retrieves local IP address of the computer as well as the gateway IP. If the gateway is something like 198.xxx.xxx.1, then the IP Address assigned to a device 
connected to that gateway will be 198.xxx.xxx.1xx.
2. Retrieves the public IP Address of device. Basically a check on if the device is connected to the internet. If this step fails (no available Public IP), then 
program quits .
3. If step 2 is successful, the access point is able to provide the device with internet connection. Then we do nameservers check (NS lookup) and IP Address of 
a particular domain (like google.com). Meant to check whether device can access online content through DNS.
4. Websocket connectivity Test - Tests whether device can open and maintain a websocket connection.
5. In this step, we check whether a particular domain and port is listening to TCP/UDP signals. The domains and port are to be listed in a config.json.
6. Logs all of the info
7. All tests successful.!


[Logging example](https://user-images.githubusercontent.com/26086224/199232311-3d9cf358-0e00-4e6a-bd7d-aad74e472265.png)
![Program results](https://user-images.githubusercontent.com/26086224/199235475-46b7a780-4dd1-48f0-92a4-24f2b268a26f.png)
