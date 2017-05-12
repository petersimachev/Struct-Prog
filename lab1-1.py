import math
print('Сейчас будет решено выражение:')
print('P = e^(y+5.5)+9.1*h^3')
y = float(input('Введите переменную y: '))
h = float(input('Введите переменную h: '))
P = math.exp(y+5.5)+9.1*math.pow(h,3)
print('Порядок решения:')
print('1) ',y,'+ 5,5; 2) e ^',y+5.5,'; 3)',h,'^ 3; 4)',math.pow(h,3),'* 9.1; 5)',math.exp(y+5.5),'+',9.1*math.pow(h,3))
print('Ответ равен:',P)
