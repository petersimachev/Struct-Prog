a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
c=int(input("Введите третье число: "))
max=int(0)

if a>=b :
    max=a
else: max=b
if c>=max:
    max=c
print(max)