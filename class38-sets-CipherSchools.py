#Sets-Unoderded collection of unique elements.
s = {1,3,4,5}
s.add(2)
s.add(1)
s.add(6)
print(s)
s.remove(4)# it removes the element from the set but it give error when the element is not present in the set.
print(s)
s.discard(10)#it also deletes the element from the set but it doesn't give error when the element is not present in the set.
print(s)
s1 = s.copy()
print(s1)

# More functions on Set.
a = {'a','b','c'}
if 'a' in s:
    print("present")
else:
    print("not present")


#UNION and INTERSECTION

set1 = {1,2,3,4}
set2 = {3,4,5,6,7}

# union :- |(pipe)
# intersection:- & (and)

union_set = set1.union(set2)
print(union_set)

union_set2 = set1 | set2
print(union_set2)

inter_set = set1.intersection(set2)
print(inter_set)

inter_set2 = set1 & set2
print(inter_set2)

