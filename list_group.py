with open("/etc/group", "r") as file:
    groups = file.read().splitlines()


def get_group_members(group_name):
    for line in groups:
        parts = line.split(":")

        if parts[0] == group_name:
            print(parts)

