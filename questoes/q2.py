n = 21

t1 = 0
t2 = 1
t3 = t1 + t2

cont = 3
while t3 <= n:
    print('  - {}'.format(t3), end='')
    if n == t3:
        print('\nO número {} está na sequência de Fibonacci.'.format(n))
        break
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    cont += 1
else:
    print('\nSeu número não se encontra nesta sequência.')

n = 25

t1 = 0
t2 = 1
t3 = t1 + t2

cont = 3
while t3 <= n:
    print('  - {}'.format(t3), end='')
    if n == t3:
        print('\nO número {} está na sequência de Fibonacci.'.format(n))
        break
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    cont += 1
else:
    print('\n0 número {} não se encontra nesta sequência.'.format(n))