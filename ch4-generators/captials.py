def get_capitals():
    with open('capitals.txt', 'r') as file:
        lines = (line for line in file)
        tuples = (line.replace("\n",'').split(",") for line in lines)
        capitals = dict(tuples)
        return capitals
    
capitls = get_capitals()
print(capitls["Israel"])