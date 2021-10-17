menu  = {
    'Veg manchurian' : 189.00,
    'Fried Rice' : 100.00,
    'Veg momos': 80.00
}

new_menu = {
    'Chicken Manchurian' : 259.00,
    'Chicken Momos' : 160.00
}

print('before update', menu)
menu.update(new_menu)

print('after update', menu)

update_menu = {
    'Veg momos': 100.00,
    'Veg Chowmein' : 120.00
}

menu.update(update_menu)
print('final menu', menu)

