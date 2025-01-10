#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Faktöriyel negatif bir sayı için tanımlı değildir.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: ./script.py <pozitif tam sayı>")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        print(factorial(num))
    except ValueError as e:
        print(f"Hata: {e}")
        sys.exit(1)
