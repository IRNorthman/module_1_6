my_dict={"Anna":1998, "Lucy":2002, "Egor":2004, 'Katya':1996}
print(my_dict)
print(my_dict.get('Egor'))
print(my_dict.get("Pasha"))
my_dict.update({'Pasha': 1995,
                'Lana':1991})
L = my_dict.pop('Lucy')
print(L)
print(my_dict)

my_set={1,2,'ALARM','ALARM',2,1}
print(my_set)
my_set.add(4)
my_set.add('WOW')
my_set.discard(2)
print(my_set)