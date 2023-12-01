import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("MOLOTOV'S PORT SCANNER")
print(ascii_banner)

target = input(str("Target IP:"))

print("_" * 50)
print("Scanning Target: " + target)
print("Scanning Started at: " + str(datetime.now()))
print("_" * 50)

try:

    #Scans every port on the ip
    for port in range (1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #Shows open ports
        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open".format(port))
            s.close()
except KeyboardInterrupt:
    print("\n Stopping")
    sys.exit()

except socket.error:
    print("\ Host not responding")
    sys.exit()