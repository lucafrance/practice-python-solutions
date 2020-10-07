
file_name = "Training_01.txt"

paths_list = open(file_name, "rt").read().splitlines(False)

category_count = {}
for path in paths_list:
    category = path.split(sep="/")[2]
    if category not in category_count:
        category_count[category] = 0
    category_count[category] += 1

print(category_count)
