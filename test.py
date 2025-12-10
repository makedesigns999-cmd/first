a={"val1":[1,2,3,[4,5]]}
a=[1,2,3,4,5,[6,7]]
a[0]=9
print(a)

c=a.copy()

print(id(c))
print(id(c[5]))

c[5]=6

print(c)


mixed_list = [3, 'apple', 2.5, True, 'banana', 1, False]

 
op= [False, True, 2.5, 1, 3, 'apple', 'banana']

l1= ['python','is','fun'] 

l1.sort(key=lambda x:len(x))
print(l)
