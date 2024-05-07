def parse_ranges(string:str):
    return ((a,b) for (a,b) in (tu.split("-") for tu in string.split(",")))

ls = []
for (a,b) in parse_ranges("1-2,6-8"):
    for num in range(int(a),int(b)+1):
        ls.append(num)
print(ls)