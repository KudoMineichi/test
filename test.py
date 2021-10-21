

name="Kudo Mine"



for i in range(len(name)):
    print(name[len(name)-(i+1)], end='')
print()
for i in reversed(name):
    print(i, end='')
print()
print(name[::-1])
print("".join(reversed(name)))







