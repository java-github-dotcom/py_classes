def invest(amount=float, rate=float, years=int):
    for i in range(years):
        amount=amount+amount*rate
        print(f'year {i+1}: {round(amount, 2)}')

invest(100, .05, 5)


