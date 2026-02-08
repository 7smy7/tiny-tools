import sys
import socket
from datetime import datetime

# Usage: python port_scanner.py <ip>
# Basic TCP connect scan

if len(sys.argv) == 2:
    target = sys.argv[1]
else:
    print("No IP specified, scanning localhost...")
    target = "127.0.0.1"

print("-" * 50)
print(f"Scanning Target: {target}")
print("-" * 50)

try:
    # Just checking common ports for now
    for port in range(20, 100): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port}: OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nExiting.")
    sys.exit()
except socket.error:
    print("\nHost not responding.")
    sys.exit()
