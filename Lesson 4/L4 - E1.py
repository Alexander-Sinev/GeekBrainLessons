def sal():
    try:
        time = float(input('Count of hours: '))
        salary = int(input('Payment in 1 hour: '))
        bonus = int(input('Bonus payment: '))
        res = time * salary + bonus
        print(f'Payment -{res}')
    except ValueError:
        return print('Not a number!')
sal()
