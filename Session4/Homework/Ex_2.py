prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {}

stock["banana"] = 6
stock["orange"] = 32
stock["apple"] = 0
stock["pear"] = 15

for i in prices:
    print("• {0}: {1}\n• price: {2}\n".format(i, stock[i], prices[i]))

total = 0
for j in prices:
    total += prices[j] * stock[j]
    print('{0} {1}(s) cost {2}'.format(stock[j], j, stock[j] * prices[j]))
print('All fruits cost: ', total)
