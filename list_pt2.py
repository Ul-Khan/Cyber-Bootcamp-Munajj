ips = ["192.168.1.1","10.0.0.1","172.16.0.1","192.168.1.1","10.0.0.1"]
#indexing
print("first IP:",ips [0])
#slicing
print("First Two Ips:",ips[0:2])


def find_duplicates(ips_list): ["192.168.1.1","10.0.0.1","192.168.1.1"]
seen = set()
duplicates = set()
for ip in (ips_list):
    if ip in seen:
        duplicates.add
    else:
        seen.add(ip)
    if duplicates:
        print("Duplicate IPs found:", duplicates)
    else:
        print("No duplicates found.")