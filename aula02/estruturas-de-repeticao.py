from time import sleep, strftime

"""
Material complementar: http://www.devfuria.com.br/python/lacos-de-repeticao/
"""

# serie de fibonacci até 1.000.000

a = b = 1
while a < 10 ** 6:
    print(a)
    a, b = b, a + b

for letra in 'Robson':
    print(letra)

for i in range (1, 34):
    print(i**2)

# Brinde: um relogio no console
"""
while True:
    h = strftime('%H:%M:%S')
    print(h)
    sleep(1)

ctrl + C para interromper o script
"""
