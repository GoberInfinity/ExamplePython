# When you're trying to access and modify the elements in the current array
# you need to use: "range" instead of "in"
power_set = [[]]
for i in range(len(power_set)):
    power_set.append(power_set[i] + [0])
