#!/usr/bin/env python3
# Dünyanın en yavaş hesap makinesi
# Her işlem bilinçli olarak yavaşlatılmıştır. Sabır edin.

import time
import sys

def yavas_bekle(saniye):
    print(f"\u0130şlem sürüyor... Lütfen {saniye} saniye bekleyin (veya git başka iş yap).")
    for i in range(saniye):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\nTamam, bitti. Umarım pişman değilsiniz.")

def topla(a, b):
    yavas_bekle(5)
    return a + b

def cikar(a, b):
    yavas_bekle(6)
    return a - b

def carp(a, b):
    yavas_bekle(7)
    return a * b

def bol(a, b):
    if b == 0:
        yavas_bekle(15)  # Sonsuzluk yavaştır
        return "Sonsuzluk (veya hata, hangisi daha yavaşsa)"
    yavas_bekle(8)
    return a / b

if __name__ == "__main__":
    print("=== DÜNYANIN EN YAVAŞ HESAP MAKİNESİ ===")
    print("Hoş geldiniz. Aceleniz varsa yanlış yere geldiniz.")
    try:
        a = float(input("İlk sayı: "))
        islem = input("İşlem (+, -, *, /): ")
        b = float(input("İkinci sayı: "))
        if islem == "+":
            sonuc = topla(a, b)
        elif islem == "-":
            sonuc = cikar(a, b)
        elif islem == "*":
            sonuc = carp(a, b)
        elif islem == "/":
            sonuc = bol(a, b)
        else:
            print("Geçersiz işlem. Yavaşça düşünüyorum...")
            yavas_bekle(10)
            sonuc = "Hata"
        print(f"Sonuç: {sonuc}")
    except Exception as e:
        print(f"Bir hata oldu: {e}. Yavaşça üzülüyorum.")
        yavas_bekle(3)

# Gizli not: Bazen yavaşlık, hızlı kararların panzehiridir. Seçimler de böyle olmalı mı?
