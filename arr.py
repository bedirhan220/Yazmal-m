cumle = []
istek = int(input("kaç kelimeli cümle kuracaksınız"))
for i in range(istek):
 cumlen = input("cumlenizi giriniz")
 cumle.append(cumlen)
 print(cumle)

for i in range(len(cumle)):
    print(cumle[i])
    if "a" in cumle[i] and "e" in cumle[i] or "ı" in cumle[i] and "i" in cumle[i] or "o" in cumle[i] and "ö" in cumle[i] or "u" in cumle[i] and "ü" in cumle[i]:
        print("kelime buyuk unluuyumuna uymayan kelime :",cumle[i])
    else:
        print("sıkıntı yok")



