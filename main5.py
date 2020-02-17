#Collections 
a_set = set()
a_set.add(2)
a_set.add(3)
a_set.add(2)
b_set = set([3,"BOB",5,5])
for item in a_set.union(b_set):
    print(item,a_set.union(b_set).__sizeof__() )


#Collections str 
name = "My name is BoOOOOOOb   11123"
print(name[0], name[2])
len(name + name)
print(name * -20)


print(name[::-1])

print(name[::2])
print(dir(name))

#Collection list
b_list = [20, 30 ,40]
b_list.append(500)
b_list[1] = 30000
print(b_list)
print(type(b_list))
b_list.append([200, 300])
print(type(b_list))

name = "Привет Ёж!"


print("abcd" > "b")


#Collection tuple 
tup = (1,2,3,4)



a_list = [1,2,3,4,5,6,7,8,9,10]
a_tuple = (1,2,3,4,5,6,7,8,9,10)

print("Tuple: ", a_tuple.__sizeof__())
print("List: ", a_list.__sizeof__())

#Collection dict 
dictionary = {"one":1, "two":2, "one":10}
print(dictionary["one"])







