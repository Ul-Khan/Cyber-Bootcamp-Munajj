log = "admin, 192.168.1.1"

parts = log.split(", ")

print(parts[1])

import re

log = "Error from 192.168.1.1"

ip = re.search(r"\d+\.\d+\.\d+\.\d+", log)

print(ip.group())



