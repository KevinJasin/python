from collections import OrderedDict
me = {
    'first_name': 'Kevin',
    'last_name': 'Jašin',
    'birth_year': 2005,
    'place_of_living': 'Tallinn',
    'dessert': 'Ice cream'
}

#print(me.get('place_of_living'))
#print(me['place_of_living'])

me['dessert'] = 'Brownie'
me['personal_code'] = '12234344'
me.pop("birth_year")
me['height'] = '1.80'
me = OrderedDict(reversed(list(me.items())))

for k, v in me.items():
    print(k, v)

if 'personal_code' in me:
    print('isikukood on olemas')
else:
    print('isikukoodi ei ole')
print(len(me)) 
    
