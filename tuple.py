# Create a tuple (immutable sequence)
log_entry = ("192.168.1.1", 80)
#Access elements by index
print(log_entry[0])

# Tuples are immutable - this will cause a error
# Uncomment to see the error
# log_entry[0] = "10.0.0.1"

# checking tuple length
print("tuple length:",len(log_entry))