def find_same_name(array):
    name_dict = dict()
    result = set()
    for name in array:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)
    return result
        

name = ["Tom","Jerry","Mike","Tom"]
print(find_same_name(name))

name2 = ["Tom","Jerry","Mike","Tom","Alex","Tom","Mike"]
print(find_same_name(name2))


