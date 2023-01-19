me = {
    'first_name': 'Kevin',
    'last_name': 'Jašin',
    'birth_year': 2005,
    'place_of_living': 'Tallinn',
    'dessert': 'Ice cream'
}

print(me.get('place_of_living'))
print(me['place_of_living'])

me['dessert'] = 'Brownie'

for k, v in me.items():
    print(k, v)

    me['personal_code'] = '1234567890'

   if 'personal_code' in me:
       print('isikukood on olemas')
   else:
    print()


