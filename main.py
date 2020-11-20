cevap_anahtarı = []
eleman = int(input("sınavınız kaç sorulu olacak ? "))
for i in range(eleman):
    cevap_anahtarı.append(i)

for i in range(0,len(cevap_anahtarı)):
    cevap_anahtarı[i] = input("{}.sorunun cevabı".format(i))

puan = 0
cevaplar = [1,2,3,4,4]
for i in range(0,len(cevap_anahtarı)):
    cevaplar[i] = input("{}.sorunun cevabı".format(i))
    if cevaplar[i] == cevap_anahtarı[i]:
        puan = puan + 20
    elif cevaplar[i] != cevap_anahtarı[i]:
        puan = puan
    else:
        print("hata")

print("öğrencinin aldığı not",puan)
print("cevap anahtarı :",cevap_anahtarı)
print("senin verdiğin cevaplar :",cevaplar)

