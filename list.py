ips = ["192.168.1.1","10.0.0.1"]
ips.append("172.16.0.1")
ips.remove("10.0.0.1")
ips.sort
print(ips)

# List comprehension: filter IPs containing "192"
sorted_ips=[ip for ip in ips if "192" in ip]
#print("Filtered IPs:",sorted_ips)

print("Filtered IPs:",sorted_ips)

numbers = [1,2,3,4]
doubled = [x*2 for x in numbers]
print("Doubled numbers:",doubled)
