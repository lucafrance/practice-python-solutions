

file_name = "nameslist.txt"

names_list = open(file_name, "rt").read().splitlines(False)
print(names_list)

names_count = {}
for name in names_list:
    if name not in names_count:
        names_count[name] = 0
    names_count[name] += 1

print(names_count)