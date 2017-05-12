print("Сейчас будут решена функция:")
print("y = sh(x)*tg(x+1)-tg^2(2+sh(x-1))")
print("Где sh(x) = (e^x-e^-x)/2")
x=float(input("Введите аргумент x: "))
import math
sh=(math.exp(x)+math.exp(-x))/2
print("Sh(x) = ",sh)
y=sh*math.tan(math.radians(x)+1)-math.pow(math.tan(2+((math.exp(x-1)+math.exp(-x-1))/2)),2)
print("Функция y = ",y)