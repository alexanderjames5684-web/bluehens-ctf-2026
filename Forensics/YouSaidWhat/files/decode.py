"""
Blue Hens CTF 2026 - You Said What?
Extracts and decodes the hex string identified in the packet capture.
"""

import re


def extract_and_decode(pcap_path):
    with open(pcap_path, "rb") as f:
        data = f.read()

    hex_match = re.search(b"6e6f626f647[0-9a-f]+", data)

    if hex_match:
        raw_hex = hex_match.group().decode()
        decoded = bytes.fromhex(raw_hex).decode()
        print(f"Hex found:       {raw_hex}")
        print(f"Decoded message: {decoded}")
        print(f"Use as ZIP password: {decoded}")
    else:
        print("No hex string found in capture.")


if __name__ == "__main__":
    extract_and_decode("yousaidwhat.pcapng")
