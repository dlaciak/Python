Wiek = int(input("Ile masz lat?\n"))
if Wiek < 18:
    print("Jesteś niepełnoletni. Będziesz pełnoletni za {} lat" .format(18-Wiek))
elif Wiek > 100:
    print("200 lat ♫, 200 lat ♫, 200 lat ♫, Niech żyje, żyje nam")
else:
    print("Jesteś pełnoletni")
