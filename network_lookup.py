"""Display basic network information for an IPv4/IPv6 address or CIDR."""

import argparse
import ipaddress


def main():
    parser = argparse.ArgumentParser(description="Explain an IP address and subnet.")
    parser.add_argument("address", help="Example: 192.168.1.25/24")
    args = parser.parse_args()

    try:
        interface = ipaddress.ip_interface(args.address)
    except ValueError as error:
        parser.error(f"Invalid address: {error}")

    network = interface.network
    print(f"IP address:       {interface.ip}")
    print(f"IP version:       IPv{interface.version}")
    print(f"Network:          {network}")
    print(f"Prefix length:    /{network.prefixlen}")
    print(f"Netmask:          {network.netmask}")
    print(f"Broadcast:        {network.broadcast_address}")
    print(f"Private address:  {interface.ip.is_private}")
    print(f"Loopback:         {interface.ip.is_loopback}")


if __name__ == "__main__":
    main()
