#Zip function
# it combines the two lists...
user_id = ['user1','user2','user3','user4']
first_name = ['Shivam','Kunal','Ramandeep','Samir']
last_name = ['Yadav','Singh','Raj','Maverick']
print(list(zip(user_id,first_name,last_name)))

# * operator with  zip
l = [(1,2),(3,4),(5,6),(7,8)]
l1,l2 = list(zip(*l))
print(list(l1))
print(list(l2))

list1 = [1,3,13,8]
list2 = [2,1,7,9]
new_list=[]

for pair in zip(list1,list2):
    new_list.append(max(pair))
print(new_list)
    