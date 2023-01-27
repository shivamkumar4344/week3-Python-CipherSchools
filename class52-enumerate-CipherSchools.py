# Without enumerate
# names = ["Shivam","Samir","Kunal","Ramandeep"]
# pos = 0
# for x in names:
#     print(f"{pos}------>{x}")
#     pos+=1

# With ennumerate

names = ["Shivam","Samir","Kunal","Ramandeep"]
for pos,x in enumerate(names):
    print(f"{pos}------>{x}")

# Find the postion of the item from the list and if it is not present return "-1"   
def find_pos(l, target):
    for pos,x in enumerate(l):
        if x == target:
            return pos
    return -1

print(find_pos(names,"Samir"))

print(find_pos(names,"abc"))