def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
        
d = {'name':'Shivam','age':19,'Add':'Khagaul','City':'Patna','fav_movie':'KGF2'}
func(**d)


        