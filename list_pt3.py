def find_duplicates(ips_list):
    seen = set()
    duplicates = set()

    for ip in ips_list:
        if ip in seen:
            duplicates.add(ip)
        else:
            seen.add(ip)
    if duplicates:
        print("Duplicate IPs found:", duplicates)
    else:
        print("No duplicates found.")

ips = ["192.168.1.1","10.0.0.1","192.168.1.1"]
find_duplicates(ips)