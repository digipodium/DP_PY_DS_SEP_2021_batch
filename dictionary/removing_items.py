hotel_menu = {
    'Veg manchurian': 189.0,
    'Fried Rice': 100.0,
    'Veg momos': 100.0,
    'Chicken Manchurian': 259.0,
    'Chicken Momos': 160.0,
    'Veg Chowmein': 120.0,
    'Costly Food Item 1': 999.00
    }

# remove
if 'Costly Food Item 1' in hotel_menu:
    rmv_value = hotel_menu.pop('Costly Food Item 1')
    print(rmv_value)
    print(hotel_menu)

rand_val = hotel_menu.popitem()
print(rand_val)
print(hotel_menu)

hotel_menu.clear()
print(hotel_menu)
