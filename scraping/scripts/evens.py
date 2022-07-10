def evens():

    '''
        Imprime los primeros 100 números pares
        utilizando un generador...
    '''

    n = 1
    even = 0

    while(n <= 100):
        yield even
        even += 2
        n += 1

n = 1
numbers = evens()
while(n <= 100):
    print(next(numbers))
    n += 1