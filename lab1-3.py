import math
print('Сейчас будет решено выражение:')
print('N = (z+(z*x)^(1/5))^(1/5))/e^x+a^5*arctg(x)')
z = float(input('Введите переменную z: '))
e = float(input('Введите переменную e: '))
x = float(input('Введите переменную x: '))
a = float(input('Введите переменную a: '))
sqrz=z+math.sqrt(z*x)
n=math.pow(sqrz,1/5)/(math.exp(x)+math.pow(a,5)*math.atan(math.radians(x)))
print('Ответ:',n)