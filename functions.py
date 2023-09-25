import os
import pyfiglet
import time

def secim():
    os.system("clear")
    figlet_kutay = pyfiglet.figlet_format("KUTAYKOCA  Hack - Tool", font="standard")
    print(figlet_kutay + "versiyon 1.0\n\n")

    print("1 - Mac Adresi Değiştirmek")
    print("2 - Bilgi Toplama")
    print("3 - Ağ Taramaları")
    print("4 - Hedefte Çıkmış Zafiyet Taraması")
    print("5 - Hedefte Web Zafiyeti Bulma (XSS, SQL)")
    print("6 - Görsel Analiz")
    print("7 - Wordpress Siteleri Tarama")
    print("8 - Kişiye Özel Wordlist Oluşturma ")


def getMac():
    kelime = input("\nMac adresini değiştirmek istediğin interface giriniz(eth0,wlan0): ")
    os.system("macchanger -r " + kelime)


def infoinfo():
    os.system("clear")
    print("1 - Dmitry Aracı İle Bilgi Toplama")
    print("2 - TheHarvester Aracı İle Bilgi Toplama")
    print("3 - Local Ağdaki Cihazları Göster")
    print("4 - Hedef Adreste Güvenlik Duvarı Kontrol")
    print("5 - Dizin Taraması")
    print("6 - DNS Taraması")

    bilgisecim = input("\nBilgi Toplanmak İstenen Aracı Seçiniz: ")

    if bilgisecim == "1":
        dmtirysorgu = input("Sorgulancak Alan Adını girin(www.site.com): ")
        os.system(f"dmitry -winsep {dmtirysorgu}")

    elif bilgisecim == "2":
        harvester = input("Sorgulancak Alan Adını girin: ")
        os.system(f"theHarvester -d {harvester} -l 500 -b all")

    elif bilgisecim == "3":
        os.system("netdiscover")

    elif bilgisecim == "4":

        wafwoof = input("Alan Adını Giriniz: ")
        os.system(f"wafw00f -a {wafwoof}")


    elif bilgisecim == "5":
        dirb = input("Dizin Sorgusu Yapılacak Sitesi Linki: ")
        os.system(f"dirb {dirb}")


    elif bilgisecim == "6":
        dnsenum = input("DNS Sorgusu Yapılacak Adres: ")
        os.system(f"dnsenum {dnsenum}")

    else:
        print("Hatalı Seçim Yaptınız! Tekrar Deneyiniz")


def nmapscan():
    os.system("clear")
    print("1 - Nmap Servis ve Versiyon Taraması")
    print("2 - Nmap İle Script Taraması")
    print("3 - Nmap ile Ayrıntılı Tarama")
    print("4 - Nmap ile Tüm TCP Portları Tara")
    print("5 - Nmap ile Tüm UDP Portları Tara")
    print("6 - Nmap ile Hedef İşletim Sistemi Tespiti")

    nmapsorgu = input("\nYapmak İstediğiniz İşlemi Seçiniz: ")

    if nmapsorgu == "1":
        nmap = input("Tarama Yapılacak IP adresi: ")
        print("Lütfen Bekleyiniz...")
        os.system(f"nmap -sS -sV {nmap}")
        time.sleep(1000)  # ------------------- geçiçi çözüm olarak sleep iş görür fakat yeni çözüm şart

    elif nmapsorgu == "2":
        nmap = input("Tarama Yapılacak IP adresi: ")
        print("Lütfen Bekleyiniz...")
        os.system(f"nmap -sC {nmap}")

    elif nmapsorgu == "3":
        nmap = input("Tarama Yapılacak IP adresi: ")
        print("Lütfen Bekleyiniz...")
        os.system(f"nmap -A {nmap}")

    elif nmapsorgu == "4":
        nmap = input("Tarama Yapılacak IP adresi: ")
        print("Lütfen Bekleyiniz...")
        os.system(f"nmap -sT {nmap}")

    elif nmapsorgu == "5":
        nmap = input("Tarama Yapılacak IP adresi: ")
        print("Lütfen Bekleyiniz...")
        os.system(f"nmap -sU {nmap}")

    elif nmapsorgu == "6":
        nmap = input("Tarama Yapılacak IP adresi: ")
        print("Lütfen Bekleyiniz...")
        os.system(f"nmap -O {nmap}")


def searchsploit():
    os.system("clear")
    searchplt = input("Zafiyet Aranacak Anahtar Kelime(Ör: Vsftpd): ")
    os.system(f"searchsploit {searchplt}")


def niktoscan():
    os.system("clear")
    print("1 - Web Sitesine Yönelik Standart Tarama")
    print("2 - SQL Injection Taraması")
    print("3 - XSS Taraması")

    niktosearch = input("\nYapmak İstediğiniz İşlemi Seçiniz: ")

    if niktosearch == "1":
        searchnikto = input("Tarama Yapılacak URL Adresini Giriniz: ")
        os.system(f"nikto -h {searchnikto}")

    elif niktosearch == "2":
        searchnikto = input("Tarama Yapılacak URL Adresini Giriniz: ")
        os.system(f"nikto -h {searchnikto} -Cgidirs none -Tuning 9")

    elif niktosearch == "3":
        searchnikto = input("Arama Yapılacak URL Adresini Giriniz: ")
        os.system(f"nikto -h {searchnikto} -Cgidirs none -Tuning 4")


def exiftool():
    os.system("clear")
    exiftool = input("Analiz Yapılacak Resim Yolu: ")
    os.system(f"exiftool {exiftool}")


def wordpress():
    os.system("clear")
    print("1 - Hedef Siteye Yönelik Genel Tarama")
    print("2 - Hedef Sitenin Eklentilerini Tespit Etmek")
    print("3 - Kullanılan Tema Üzerindeki Açıklar")
    print("4 - Sitede Kullanılan Tema Bilgisi")

    wordinput = input("\nYapmak İstediğiniz İşlemi Seçiniz: ")

    if wordinput == "1":
        scanpress = input("Taranacak Site: ")
        os.system(f"wpscan --url {scanpress}")

    elif wordinput == "2":
        scanpress = input("Taranacak Site: ")
        os.system(f"wpscan --url {scanpress} --enumerate p")

        eklentitarama = input("Bulunan Eklentilerin Zafiyetleri Taransın mı? (e veya h): ")
        if eklentitarama == "e":
            os.system(f"wpscan --url {scanpress} --enumerate ap")

        elif eklentitarama == "h":
            print("Çıkış Yapıldı")
        else:
            print("Hatalı İşlem Yaptınız")

    elif wordinput == "3":
        scanpress = input("Taranacak Site: ")
        os.system(f"wpscan --url {scanpress} --enumerate at")

    elif wordinput == "4":
        scanpress = input("Taranacak Site: ")
        os.system(f"wpscan --url {scanpress} --enumerate t")


def wordlist():
    os.system("clear")
    print("Oluşturulacak Wordlist için Parametleri Giriniz\n")
    min = input("Wordlistiniz Minimum Kaç Karakter İçersin: ")
    max = input("Wordlistiniz Maximum Kaç Karakter İçersin: ")
    icerik = input("Wordlistiniz Hangi Karakterleri İçersin: ")
    dosyaismi = input("Wordlist Dosyanızın İsmi: ")
    os.system(f"crunch  {min} {max} {icerik} -o {dosyaismi}")