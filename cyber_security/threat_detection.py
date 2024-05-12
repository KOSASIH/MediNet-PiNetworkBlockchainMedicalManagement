import os
import sys
import time
import socket
import scapy.all as scapy
from scapy.layers import http
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sendp, sr1
from scapy.utils import RandShort, RandInt

def detect_threats(interface: str) -> None:
    """
    Detect threats and prevent intrusions on the network.

    Args:
        interface (str): The network interface to monitor.
    """
    # Set the network interface
    scapy.config.conf.iface = interface

    # Set the packet filter
    filter = 'tcp and (port 80 or port 443)'

    # Set the packet counter
    packet_counter = 0

    # Set the maximum number of packets to analyze
    max_packets = 10000

    # Set the start time
    start_time = time.time()

    # Analyze packets
    while True:
        # Sniff packets
        packet = scapy.sniff(filter=filter, count=1, timeout=1)

        # Increment the packet counter
        packet_counter += 1

        # Check if the maximum number of packets has been reached
        if packet_counter >= max_packets:
            break

        # Check if the packet is an HTTP request
        if packet.haslayer(http.HTTPRequest):
            # Check if the request contains malicious payloads
            if 'sql' in packet.getlayer(http.HTTPRequest).fields['Host'] or 'xss' in packet.getlayer(http.HTTPRequest).fields['Host']:
                # Print a warning message
                print(f'Warning: Potential SQL injection or XSS attack detected from {packet.getlayer(IP).src}')

                # Send a TCP reset packet to the source IP address
                reset_packet = IP(dst=packet.getlayer(IP).src, src=packet.getlayer(IP).dst) / TCP(sport=packet.getlayer(TCP).dport, dport=packet.getlayer(TCP).sport, flags='R')
                sendp(reset_packet, iface=interface)

        # Check if the packet is an HTTP response
        elif packet.haslayer(http.HTTPResponse):
            # Check if the response contains malicious payloads
            if 'sql' in packet.getlayer(http.HTTPResponse).fields['Content-Type'] or 'xss' in packet.getlayer(http.HTTPResponse).fields['Content-Type']:
                # Print a warning message
                print(f'Warning: Potential SQL injection or XSS attack detected from {packet.getlayer(IP).src}')

                # Send a TCP reset packet to the source IP address
                reset_packet = IP(dst=packet.getlayer(IP).src, src=packet.getlayer(IP).dst) / TCP(sport=packet.getlayer(TCP).dport, dport=packet.getlayer(TCP).sport, flags='R')
                sendp(reset_packet, iface=interface)

        # Print the elapsed time
        elapsed_time = time.time() - start_time
        print(f'Elapsed Time: {elapsed_time:.2f} seconds')

def prevent_intrusion(interface: str) -> None:
    """
    Prevent intrusions on the network by blocking known malicious IP addresses.

    Args:
        interface (str): The network interface to monitor.
    """
    # Set the network interface
    scapy.config.conf.iface = interface

    # Set the packet filter
    filter = 'tcp and (port80 or port 443)'

    # Load the list of known malicious IP addresses
    with open('malicious_ips.txt', 'r') as f:
        malicious_ips = f.read().splitlines()

    # Set the packet counter
    packet_counter = 0

    # Set the maximum number of packets to analyze
    max_packets = 10000

    # Set the start time
    start_time = time.time()

    # Analyze packets
    while True:
        # Sniff packets
        packet = scapy.sniff(filter=filter, count=1, timeout=1)

        # Increment the packet counter
        packet_counter += 1

        # Check if the maximum number of packets has been reached
        if packet_counter >= max_packets:
            break

        # Check if the source IP address is in the list of known malicious IP addresses
        if packet.getlayer(IP).src in malicious_ips:
            # Print a warning message
            print(f'Warning: Intrusion detected from {packet.getlayer(IP).src}')

            # Drop the packet
            packet.drop()

        # Print the elapsed time
        elapsed_time = time.time() - start_time
        print(f'Elapsed Time: {elapsed_time:.2f} seconds')
