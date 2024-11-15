def factors():
    n = int(input('Enter a positive integer: '))
    for i in range(n+1):
        try:
            if n%i == 0:
                print(f'{i} is a factor of {n}')
            else: 
                continue
        except ZeroDivisionError:
            pass

factors()