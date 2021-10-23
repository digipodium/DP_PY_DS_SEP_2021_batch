# required parameter
def triangle(b,h):
    return 1/2 * b * h

# triangle() -> TypeError: triangle() missing 2 required positional arguments: 'b' and 'h'

def bike(petrol):
    while petrol > 0:
        print("Wrr Wrr Wrroooooom")
        petrol -=1
    print("phir se petrol bharo")

# bike() -> TypeError: bike() missing 1 required positional argument: 'petrol'
bike(21)