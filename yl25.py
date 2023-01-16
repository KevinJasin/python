me = {
    'first_name': 'Kevin',
    'last_name': 'Jašin',
    'birth_year': 2005,
    'place_of_living': 'Tallinn',
    'dessert': 'Ice cream'
}

print(me.get('place_of_living'))
print(me['place_of_living'])

me['dessert'] = 'Ice cream'

for k, v in me_items():
    print(k, v)
