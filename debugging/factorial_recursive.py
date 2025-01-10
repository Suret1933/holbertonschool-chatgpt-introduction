#!/usr/bin/python3
import sys

def factorial(n):
    """
    Fonksiyon Açıklaması:
    Bu fonksiyon, verilen pozitif tam sayının faktöriyelini hesaplar. 
    Faktöriyel, bir sayının kendisi ve kendisinden küçük pozitif tam sayıların çarpımıdır.
    Örneğin, 5! = 5 * 4 * 3 * 2 * 1 = 120.

    Parametreler:
    n (int): Faktöriyelini hesaplamak istediğimiz pozitif tam sayı.
    
    İadeler:
    - Eğer n sıfırsa, 1 döndürülür çünkü 0! = 1 olarak kabul edilir.
    - Eğer n sıfırdan büyükse, n * (n-1)'in faktöriyelini döndürerek rekürsif (öz yinelemeli) olarak işlem yapılır.
    """
    if n == 0:
        return 1  # 0! = 1 olduğu için direkt olarak 1 döndürülür.
    else:
        return n * factorial(n - 1)  # Rekürsif çağrı yaparak faktöriyel hesaplanır.

# Kullanıcıdan gelen argümanı al ve faktöriyelini hesapla
f = factorial(int(sys.argv[1]))

# Hesaplanan faktöriyel değeri ekrana yazdırılır.
print(f)

