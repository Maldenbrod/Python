k=int(input("������� ������ �� �����):\n"))
okon = ("")
if k <= 0:
    print("�� ������ �� �����?!")
    exit()
elif k == 1:
    okon = ("")
elif 1 < k < 5:
   okon = ("�")
else:
    okon = ("��")
str(okon)

print("�� �����", k, "����"+okon+"?")