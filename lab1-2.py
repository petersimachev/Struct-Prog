import math
print('Сейчас будет решено выражение:')
print('Q = sqrt(k+2,6*p*sin k)/x-d^3')
d = float(input('Введите переменную d: '))
k = float(input('Введите переменную k: '))
x = float(input('Введите переменную x: '))
p = float(input('Введите переменную p: '))
q = (math.sqrt(k+2.6*p*math.sin(k)))/(x-math.pow(d,3))
print('Порядок решения:')
print('1) sin',k,'; 2)',p,'* sin',k,'; 3)',k,'+',2.6*p*math.sin(k),'; 4) sqrt(',k+2.6*p*math.sin(k),'); 5)',d,'^3; 6)',x,'-',math.pow(d,3),'; 7)', (math.sqrt(k+2.6*p*math.sin(k))),'/',x-math.pow(d,3))
print('Ответ равен:',q)