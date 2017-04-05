god = int(input("Введите год: "))
print("Ваш год ", god)
if god%4 ==0 and god%100 >0 and god%400 ==0:
    print("visokosnyi")
else:print("ne visokosnyi")