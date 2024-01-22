#Aynı örneği, öğrencilerini listelemek isteyen bir öğretmen için siz yapınız. (Öğrenci isimleri)
ogrenciIsimleri=["Ali","veli","haydar"]
print(ogrenciIsimleri)
#print(ogrenciIsimleri[0])
#print(ogrenciIsimleri[1])
#print(ogrenciIsimleri[2])

for ogrenci in ogrenciIsimleri:
  print(ogrenci)
  #o anki gezdiği değer ogrenci buna takma ad olan alias denir

#1 den 10 a kadar dönen bir döngü
for i in range(10):
  print(i)
#1 den 10 a kadar dönen bir döngü range de verilen 10 değeri dahil değil 0 dan 9 a kadar basar
#bu örneği milyonlarc ürünü olan bir e-tic sistemindeki bir sayfada sadece 10 tane ilgili ürünü göster

for i in range(len(ogrenciIsimleri)):
  print(ogrenciIsimleri[i])

for i in range(3,10):
  print(i)
#3 dahil 10 dahil değil

for i in range(0,10,2):
  print(i)
#0 dan başla dahil 10 dahil değil çift sayıları yaz