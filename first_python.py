

name = input("Enter your name: ")
print(f"Hello, {name}!")
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


Takes a list of IPs (e.g., ["192.168.1.1", "10.0.0.1", "192.168.1.1"]).
Returns unique, sorted IPs.
Example output: ["10.0.0.1", "192.168.1.1"]