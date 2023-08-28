import scapy.all as scapy
import optparse

ascii_ = """
    _   __     __  _____                                 
   / | / /__  / /_/ ___/_________ _____  ____  ___  _____
  /  |/ / _ \/ __/\__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 / /|  /  __/ /_ ___/ / /__/ /_/ / / / / / / /  __/ /    
/_/ |_/\___/\__//____/\___/\__,_/_/ /_/_/ /_/\___/_/
"""


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipaddress", dest="ip_address", help="Enter IP address to be scanned")

    (user_input, arguments) = parse_object.parse_args()
    if not user_input.ip_address:
        print("Enter IP address!")

    return user_input


def scan_network(ip):

    arp_request_packet = scapy.ARP(pdst=ip)

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packet = broadcast_packet/arp_request_packet
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()


print(ascii_)
user_ip_address = get_user_input()
scan_network(user_ip_address.ip_address)
