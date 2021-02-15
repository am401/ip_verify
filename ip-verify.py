import ipaddress
import re

while True:
    try:
        ip = input("Enter an IP address: ")
        if re.search('/', ip):
            if ipaddress.ip_network(ip):
                print("The IP is a CIDR IP. {}".format(ip))
                continue
        elif ipaddress.ip_address(ip).is_loopback:
            print("The IP address is a loopback address: {}".format(ip))
            continue
        elif ipaddress.ip_address(ip).is_private:
            print("The IP address is a private IP: {}".format(ip))
            continue
        elif ipaddress.ip_address(ip):    
            print("The IP address is valid: {}".format(ip))
            continue
    except ValueError:
        print("ValueERROR. The IP address is invalid")
        continue
