def convert_cel_to_far():
    c = int(input('Enter a temperature in degrees C: '))
    f = c*(9/5)+32
    print(f'{c} degrees in C = {round(f, 2)} degrees in F')

def convert_far_to_cel():
    f = int(input('Enter a temperature in degrees F: '))
    c = (f-32)*5/9
    print(f'{f} degrees in F = {round(c, 2)} degrees in C')

convert_cel_to_far()
convert_far_to_cel()





