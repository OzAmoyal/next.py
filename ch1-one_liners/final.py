import functools
names = [name[:-1] for name in open('names.txt').readlines()]

def longest_name(names):
    print(sorted(names,key=lambda name:len(name),reverse=True)[0])
def sum_lengths(names):
    print(functools.reduce(lambda y,x:y+len(x),names,0))
def shortest_names(names):
    shortest_len=len(sorted(names,key=lambda name:len(name))[0])
    shortest=[name for name in names if len(name)==shortest_len]
    print('\n'.join(shortest))
def write_lengths(names):
    file=open('name_length.txt','w')
    list(map(lambda name:file.write(str(len(name))+"\n"),names))
    file.close()
def names_in_length(names):
    length=int(input("Enter Name Length: "))
    list(map(lambda name: print(name),[name for name in names if len(name)==length]))
longest_name(names)
sum_lengths(names)
shortest_names(names)
write_lengths(names)
names_in_length(names)

