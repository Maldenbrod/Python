k=int(input("Сколько грибов вы нашли):\n"))
okon = ("")
if k <= 0:
    print("Вы ничего не нашли?!")
    exit()
elif k == 1:
    okon = ("")
elif 1 < k < 5:
   okon = ("а")
else:
    okon = ("ов")
str(okon)

print("Вы нашли", k, "гриб"+okon+"?")