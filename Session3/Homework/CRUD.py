clothes_list = ['T-shirt', 'Sweater']

while True:
    i = input("Welcome to our shop, what do you want (C, R, U, D)? ")

    if i.upper() == "C":
        create = input("Enter new item: ")
        clothes_list.append(create)
        print("Our items: ", *clothes_list, sep = ", ", end = ".")

    elif i.upper() == "R":
        print("Our items: ", *clothes_list, sep = ", ", end = ".")

    elif i.upper() == "U":
        position = int(input("Update position: "))
        position = position - 1
        update_item = input("New item: ")
        clothes_list[position] = update_item
        print("Our items: ", *clothes_list, sep = ", ", end = ".")

    elif i.upper() == "D":
        print("Our items: ", *clothes_list, sep = ", ", end = ".")
        position = int(input("Delete position? "))
        del clothes_list[position - 1]
        print("Our items: ", *clothes_list, sep = ", ", end = ".")

    else:
        break
