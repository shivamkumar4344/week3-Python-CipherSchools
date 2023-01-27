name = ['Shivam Yadav','rohit','kar98K','x']
print(min(name,key=lambda item : len(item)))


students = [
    {'name':'Shivam', 'age':19,'score':36},
    {'name':'Raman','age':26,'score':56},
    {'name':'Kunal','age':20,'score':87},
    {'name':'Samir','age':22,'score':20}
]

print(max(students,key=lambda item : item.get('score')))