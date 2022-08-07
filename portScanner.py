import socket
from IPy import IP
from termcolor import colored


def scan(target, port_range):
    converted_ip = check_ip(target)
    print(colored("\n" + "Scanning the target IP/s " +
          str(target), "cyan", attrs=['bold']))
    for port in range(1, port_range):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.9)
        sock.connect((ipaddress, port))
        print(colored("[+]Open Port " + str(port), "green", attrs=['bold']))
    except:
        pass


targets = input("Enter the target " + colored("IP/s", attrs=['bold']) + ": ")
port_range = int(input("Enter the range of " +
                 colored("ports", attrs=['bold']) + " to scan: "))

if ',' in targets:
    for ip_add in targets.split(","):
        scan(ip_add.strip(" "), port_range)
else:
    scan(targets, port_range)
