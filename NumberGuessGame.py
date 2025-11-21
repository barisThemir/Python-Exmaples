import random

print ("Sayı Tahmin Oyunumuz baslıyor\n 5 Tahmin Hakkın var\n Hadi Baslayalim")

low = int(input("Alt Sınır Giriniz: "))
high = int(input("Üst Sınır Giriniz: "))

print(f"\n5 Tahmin hakkın var en düşük değer {low} ve en yüksek değer {high} Tahmin et :D")

num = random.randint(low, high)
ch = 5
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("Tahminini Gir: "))

    if guess == num:
        if gc == 1:
            print(f'Sen Fenasın hile mi yaptın yoksa Bu sayıya nasıl tek attın {num}') # Düzeltildi
        elif gc > 1:
            print(f'Tebrikler!!! Doğru Sayı {num}. {gc}. tahminde bildin') # Düzeltildi
        break # Doğru tahmin edildiğinde döngüden çıkmak için 'break' eklenmeli
        
    elif gc >= ch and guess != num:
        print(f'HAHA, Yanlış tahmin dostum sayımız {num}. Belki birdahaki sefere!')
    elif guess > num:
        print('Yükseklerdesin canım, biraz asagilardan uc')
    elif guess < num:
        print('Dostum biraz büyük dusun :D')

    # 'else: print('bitti kank')' satırı gereksizdir ve kaldırılabilir.
    # Tahmin hakkı bittiğinde zaten üstteki 'elif gc >= ch' bloğu çalışacaktır.