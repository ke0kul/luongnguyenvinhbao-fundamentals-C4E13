inventory = {
    'gold' : 500,
    'pounch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].remove('dagger')

inventory['gold'] += 50

print(inventory)
