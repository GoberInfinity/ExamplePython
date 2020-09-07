# You can supply a second parameter to enumerate to specify the number from
# which to begin counting (zero is the default).
flavor_list = ["vanilla", "chocolate", "pecan", "strawberry"]
for i, flavor in enumerate(flavor_list, 1):
    print(f"{i}, {flavor}")
