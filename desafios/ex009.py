n = int(input('Digite um Número: '))
x = 1
while x < 11:
    print('{} x {:2} = {}'.format(n, x, (n*x)))
    x += 1
else:
    print('Fim tabuada')