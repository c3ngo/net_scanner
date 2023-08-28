# Network Scanner Script

This script utilizes the Scapy library to perform network scanning by sending ARP requests to a specified IP address or IP range. It allows you to discover active hosts on the network and their corresponding MAC addresses.

## Prerequisites

- Make sure you have Python installed on your system.
- Install the Scapy library using the following command:

  ```sh
  pip install scapy
  ```

## Usage
Open a terminal and navigate to the directory containing the script.

Run the script with the following command:

  ```sh
  python3 network_scanner.py -i [ip_address]
  ```
Replace [ip_address] with the IP address or IP range you want to scan (e.g., 192.168.1.1, 192.168.1.0/24).

## Example

To scan the IP address 192.168.1.1, you would run:

  ```sh
  python3 network_scanner.py -i 192.168.1.1
  ```

To scan the IP address 192.168.1.0/24, you would run:

  ```sh
  python3 network_scanner.py -i 192.168.1.0/24
  ```

## Important Notes
This script requires administrative privileges to send ARP requests and receive responses.

The script sends ARP requests to the specified IP address or IP range. It might not work across different network segments or firewalls.
